import asyncio
from datetime import datetime, timezone
from types import SimpleNamespace

from src.ai.enricher import ContentEnricher
from src.models import ContentItem, SourceType


def _make_item() -> ContentItem:
    return ContentItem(
        id="rss:test:1",
        source_type=SourceType.RSS,
        title="Example item",
        url="https://example.com/item",
        published_at=datetime(2026, 7, 10, tzinfo=timezone.utc),
    )


def test_extract_concepts_respects_configured_query_limit() -> None:
    async def complete(**_kwargs):
        return '{"queries": ["first", "second", "third"]}'

    enricher = ContentEnricher(
        SimpleNamespace(
            config=SimpleNamespace(enrichment_max_queries=1),
            complete=complete,
        )
    )

    queries = asyncio.run(enricher._extract_concepts(_make_item(), "content"))

    assert queries == ["first"]


def test_enrichment_searches_concepts_concurrently(monkeypatch) -> None:
    enricher = ContentEnricher(SimpleNamespace())
    active_searches = 0
    max_active_searches = 0

    async def extract_concepts(_item, _content):
        return ["first", "second"]

    async def web_search(query):
        nonlocal active_searches, max_active_searches
        active_searches += 1
        max_active_searches = max(max_active_searches, active_searches)
        await asyncio.sleep(0.01)
        active_searches -= 1
        return [{"title": query, "url": f"https://example.com/{query}", "body": "body"}]

    async def translate_item(_item):
        return None

    monkeypatch.setattr(enricher, "_extract_concepts", extract_concepts)
    monkeypatch.setattr(enricher, "_web_search", web_search)
    monkeypatch.setattr(enricher, "_translate_item", translate_item)
    enricher.client.complete = lambda **_kwargs: _empty_response()

    asyncio.run(enricher._enrich_item(_make_item()))

    assert max_active_searches == 2


async def _empty_response() -> str:
    return "{}"
