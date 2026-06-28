#!/usr/bin/env python3
"""Apply branded public status labels to the live portfolio pages.

Internal status vocabulary stays simple:
- Done
- In progress
- Planned
- Idea

Public display labels are more on-brand:
- Done -> Served
- In progress -> Cooking
- Planned -> On deck
- Idea -> Spark
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
PORTFOLIO = ROOT / "portfolio.html"


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        print(f"Missing expected text, skipping: {old[:80]!r}")
        return text
    return text.replace(old, new, 1)


def patch_index() -> None:
    text = INDEX.read_text(encoding="utf-8")

    # Add branded status badge colors on the home page.
    status_rule = '.status{font-family:"Inter";font-weight:700;font-size:0.64rem;text-transform:uppercase;letter-spacing:0.08em;background:#fff;color:var(--ink);border:2px solid var(--ink);border-radius:999px;padding:4px 10px;white-space:nowrap}'
    status_rule_new = status_rule + '.status.served{background:var(--lime)}.status.cooking{background:var(--yellow)}.status.deck{background:var(--blue);color:#fff}.status.spark{background:var(--paper)}'
    if '.status.served{' not in text:
        text = replace_once(text, status_rule, status_rule_new)

    text = text.replace('Selected work · preview', 'Selected work · most finished first')
    text = text.replace('A peek at the <span class="serif">portfolio.</span>', 'Served first, <span class="serif">then cooking.</span>')
    text = text.replace('A few things I’ve shipped. <b>See the full set on the portfolio.</b>', 'Most finished cards come first. Then the work that is still cooking. <b>See the full set on the portfolio.</b>')

    # Public status labels on home cards.
    text = text.replace('<span class="status">Prototype</span>', '<span class="status served">Served</span>')
    text = text.replace('<span class="status">In production</span>', '<span class="status cooking">Cooking</span>')
    text = text.replace('<span class="status">Beta</span>', '<span class="status cooking">Cooking</span>')
    text = text.replace('🔒 Watch the film', '🔒 View pitch')
    text = text.replace('🔒 Open the app', '🔒 UI cooking')

    # Reorder preview cards: most finished first.
    match = re.search(r'(<div class="grid grid-preview">)(.*?)(\n\s*</div>\n\s*<div class="more-row">)', text, flags=re.S)
    if match:
        before, grid_body, after = match.groups()
        articles = re.findall(r'\n\s*<article class="proj .*?</article>', grid_body, flags=re.S)
        if articles:
            def rank(article: str) -> int:
                if 'AestheticSim' in article:
                    return 0
                if 'BonnetNoona' in article:
                    return 1
                if 'Aurë / Accord' in article:
                    return 2
                return 99
            sorted_articles = sorted(articles, key=rank)
            text = text[:match.start()] + before + "\n" + "\n\n".join(a.strip() for a in sorted_articles) + after + text[match.end():]
    else:
        print("Could not find grid-preview block; skipping card reorder.")

    INDEX.write_text(text, encoding="utf-8")


def patch_portfolio() -> None:
    text = PORTFOLIO.read_text(encoding="utf-8")

    text = text.replace('Cards are ordered by the same status rules used in the repos: <span class="serif">Done</span>, then <span class="serif">In progress</span>, then <span class="serif">Planned</span>, then <span class="serif">Idea</span>. If a project does not have a usable app or webapp yet, it is not labeled Done.', 'Cards are ordered by build state: <span class="serif">Served</span>, then <span class="serif">Cooking</span>, then <span class="serif">On deck</span>, then <span class="serif">Spark</span>. If a project does not have a usable app or webapp yet, it is not labeled Served.')
    text = text.replace('Done = usable/demoable', 'Served = usable/demoable')
    text = text.replace('In progress = active build', 'Cooking = active build')
    text = text.replace('Planned = scoped next', 'On deck = scoped next')
    text = text.replace('Idea = concept only', 'Spark = concept only')
    text = text.replace('Done · most finished', 'Served · most finished')
    text = text.replace('In progress · active builds', 'Cooking · active builds')
    text = text.replace('Idea · story systems', 'Spark · story systems')
    text = text.replace('<span class="status done">Done</span>', '<span class="status done">Served</span>')
    text = text.replace('<span class="status progress">In progress</span>', '<span class="status progress">Cooking</span>')
    text = text.replace('<span class="status idea">Idea</span>', '<span class="status idea">Spark</span>')
    text = text.replace('<span class="coming-soon-btn">Idea</span>', '<span class="coming-soon-btn">Spark</span>')
    text = text.replace('This needs a readable chapter UI or process demo before it becomes a portfolio app.</div><div class="builtwith">', 'This needs a readable chapter UI or process demo before it becomes a portfolio app.</div><div class="builtwith">')
    text = text.replace('Idea projects stay labeled Idea.', 'Spark projects stay labeled Spark.')

    PORTFOLIO.write_text(text, encoding="utf-8")


def main() -> None:
    patch_index()
    patch_portfolio()


if __name__ == "__main__":
    main()
