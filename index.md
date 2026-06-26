---
layout: default
title: Home
---

# Horizon

<div id="lang-zh" class="lang-section" markdown="1">

欢迎来到 [Horizon](https://github.com/thysrael/Horizon)，一个 AI 驱动的信息聚合系统。

## 文档

- [配置指南](configuration) — AI 提供商、信息源、过滤规则与环境变量替换
- [信息源采集器](scrapers) — Horizon 如何从 GitHub、Hacker News、RSS、Reddit 采集内容
- [评分系统](scoring) — 基于 AI 的内容分析与 0-10 评分体系

## 每日速递 <a class="rss-icon" href="{{ '/feed-zh.xml' | relative_url }}" aria-label="订阅中文"><svg viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M128.081 415.959c0 35.369-28.672 64.041-64.041 64.041S0 451.328 0 415.959s28.672-64.041 64.041-64.041 64.04 28.673 64.04 64.041zm175.66 47.25c-8.354-154.6-132.185-278.587-286.95-286.95C7.656 175.765 0 183.105 0 192.253v48.069c0 8.415 6.49 15.472 14.887 16.018 111.832 7.284 201.473 96.702 208.772 208.772.547 8.397 7.604 14.887 16.018 14.887h48.069c9.149.001 16.489-7.655 15.995-16.79zm144.249.288C439.596 229.677 251.465 40.445 16.503 32.01 7.473 31.686 0 38.981 0 48.016v48.068c0 8.625 6.835 15.645 15.453 15.999 191.179 7.839 344.627 161.316 352.465 352.465.353 8.618 7.373 15.453 15.999 15.453h48.068c9.034-.001 16.329-7.474 16.005-16.504z"/></svg></a>

<ul>
  {% assign zh_posts = site.posts | where: "lang", "zh" %}
  {% assign zh_count = 0 %}
  {% for post in zh_posts %}
    {% assign post_date = post.date | date: "%Y-%m-%d" %}
    {% assign path_parts = post.url | split: "/" %}
    {% assign post_file = path_parts[4] | default: "" %}
    {% if post.url contains "gmail-summary" %}
      {% assign zh_count = zh_count | plus: 1 %}
      <li><a href="{{ post.url | relative_url }}">{{ post_date }} gmail总结</a></li>
    {% elsif post_file contains "-summary-" %}
      {% assign run_time = post_file | split: "-" | first %}
      {% assign run_hour = run_time | slice: 0, 2 %}
      {% assign run_minute = run_time | slice: 2, 2 %}
      {% assign zh_count = zh_count | plus: 1 %}
      <li><a href="{{ post.url | relative_url }}">{{ post_date }} {{ run_hour }}:{{ run_minute }} AI新闻</a></li>
    {% endif %}
    {% if zh_count >= 20 %}
      {% break %}
    {% endif %}
  {% endfor %}
  {% if zh_count == 0 %}
    <li><em>暂无内容</em></li>
  {% endif %}
</ul>

</div>

<div id="lang-en" class="lang-section" markdown="1">

Welcome to [Horizon](https://github.com/thysrael/Horizon), an AI-driven information aggregation system.

## Documentation

- [Configuration Guide](configuration) — AI providers, information sources, filtering, and environment variable substitution
- [Source Scrapers](scrapers) — How Horizon collects content from GitHub, Hacker News, RSS, and Reddit
- [Scoring System](scoring) — AI-based content analysis and the 0-10 scoring scale

## Daily Digest <a class="rss-icon" href="{{ '/feed-en.xml' | relative_url }}" aria-label="Subscribe English"><svg viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M128.081 415.959c0 35.369-28.672 64.041-64.041 64.041S0 451.328 0 415.959s28.672-64.041 64.041-64.041 64.04 28.673 64.04 64.041zm175.66 47.25c-8.354-154.6-132.185-278.587-286.95-286.95C7.656 175.765 0 183.105 0 192.253v48.069c0 8.415 6.49 15.472 14.887 16.018 111.832 7.284 201.473 96.702 208.772 208.772.547 8.397 7.604 14.887 16.018 14.887h48.069c9.149.001 16.489-7.655 15.995-16.79zm144.249.288C439.596 229.677 251.465 40.445 16.503 32.01 7.473 31.686 0 38.981 0 48.016v48.068c0 8.625 6.835 15.645 15.453 15.999 191.179 7.839 344.627 161.316 352.465 352.465.353 8.618 7.373 15.453 15.999 15.453h48.068c9.034-.001 16.329-7.474 16.005-16.504z"/></svg></a>

<ul>
  {% assign en_posts = site.posts | where: "lang", "en" %}
  {% assign en_count = 0 %}
  {% for post in en_posts %}
    {% assign post_date = post.date | date: "%Y-%m-%d" %}
    {% assign path_parts = post.url | split: "/" %}
    {% assign post_file = path_parts[4] | default: "" %}
    {% if post.url contains "gmail-summary" %}
      {% assign en_count = en_count | plus: 1 %}
      <li><a href="{{ post.url | relative_url }}">{{ post_date }} Gmail digest</a></li>
    {% elsif post_file contains "-summary-" %}
      {% assign run_time = post_file | split: "-" | first %}
      {% assign run_hour = run_time | slice: 0, 2 %}
      {% assign run_minute = run_time | slice: 2, 2 %}
      {% assign en_count = en_count | plus: 1 %}
      <li><a href="{{ post.url | relative_url }}">{{ post_date }} {{ run_hour }}:{{ run_minute }} AI news</a></li>
    {% endif %}
    {% if en_count >= 20 %}
      {% break %}
    {% endif %}
  {% endfor %}
  {% if en_count == 0 %}
    <li><em>No posts yet</em></li>
  {% endif %}
</ul>

</div>
