import asyncio
from datetime import datetime, timezone
from types import SimpleNamespace

from rich.console import Console

from src.models import ContentItem, SourceType
from src.orchestrator import HorizonOrchestrator


def _item(item_id: str, title: str, tags: list[str], content: str) -> ContentItem:
    return ContentItem(
        id=item_id,
        source_type=SourceType.OPENBB,
        title=title,
        url=f"https://example.com/{item_id}",
        published_at=datetime(2026, 7, 11, tzinfo=timezone.utc),
        ai_score=8.0,
        ai_tags=tags,
        content=content,
    )


def test_topic_dedup_falls_back_to_specific_shared_tags(monkeypatch) -> None:
    orchestrator = HorizonOrchestrator.__new__(HorizonOrchestrator)
    orchestrator.config = SimpleNamespace(ai=SimpleNamespace())
    orchestrator.console = Console(record=True)
    items = [
        _item(
            "hn", "Apple sues OpenAI over trade-secret theft",
            ["Apple", "OpenAI", "trade-secrets", "AI", "legal"], "HN coverage",
        ),
        _item(
            "yahoo", "Apple reportedly sues OpenAI",
            ["Apple", "OpenAI", "Trade Secrets", "AI", "Legal"], "Yahoo coverage",
        ),
    ]

    class EmptyDedupClient:
        async def complete(self, **_kwargs):
            return '{"duplicates": []}'

    monkeypatch.setattr("src.orchestrator.create_ai_client", lambda _config: EmptyDedupClient())

    result = asyncio.run(orchestrator.merge_topic_duplicates(items))

    assert [item.id for item in result] == ["hn"]
    assert "Yahoo coverage" in result[0].content


def test_topic_dedup_does_not_merge_generic_tag_overlap() -> None:
    items = [
        _item("one", "New AI server", ["AI", "hardware", "infrastructure"], "one"),
        _item("two", "AI market outlook", ["AI", "market-analysis", "finance"], "two"),
    ]

    assert HorizonOrchestrator._find_high_confidence_tag_duplicates(items) == []
