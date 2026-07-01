#!/usr/bin/env python3
"""Update the Featured builds table in README.md with dynamic commit metadata.

Version is generated from the latest commit SHA touching the project's main source/spec path.
Last updated is generated from that same commit date.

Status vocabulary is intentionally small and consistent across repos:
- Done: usable/shipped enough to show as complete
- In progress: actively building, beta, prototype, testing, or drafting
- Planned: scoped but not started
- Idea: early concept only
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

OWNER = "N0kam0rad"
REPO = "portfolio"
README = Path("README.md")
START = "<!-- FEATURED_BUILDS:START -->"
END = "<!-- FEATURED_BUILDS:END -->"

PROJECTS = [
    {
        "name": "Aurë",
        "href": "specs/aure.html",
        "description": "Fragrance intelligence + scent wardrobe app",
        "status": "In progress",
        "path": "specs/aure.html",
    },
    {
        "name": "ACCORD",
        "href": "specs/accord.html",
        "description": "Weather-based perfume ritual automation",
        "status": "In progress",
        "path": "specs/accord.html",
    },
    {
        "name": "BonnetNoona",
        "href": "posts/how-i-built-a-consistent-ai-cast.html",
        "description": "AI-directed claymation comedy series",
        "status": "In progress",
        "path": "posts/how-i-built-a-consistent-ai-cast.html",
    },
    {
        "name": "AestheticSim",
        "href": "specs/aesthetic-sim.html",
        "description": "Facial simulation + treatment-planning platform",
        "status": "In progress",
        "path": "specs/aesthetic-sim.html",
    },
    {
        "name": "Roommate Tracker",
        "href": "specs/roommate-tracker.html",
        "description": "Shared-rent and payment tracker",
        "status": "Done",
        "path": "specs/roommate-tracker.html",
    },
    {
        "name": "My Plate Planner",
        "href": "specs/plate-planner.html",
        "description": "Diet-aware meal planner + grocery helper",
        "status": "Done",
        "path": "specs/plate-planner.html",
    },
    {
        "name": "Interior Render Studio",
        "href": "specs/interior-render.html",
        "description": "AI room rendering and style exploration tool",
        "status": "In progress",
        "path": "specs/interior-render.html",
    },
    {
        "name": "Luna’s Rituals",
        "href": "specs/luna-rituals.html",
        "description": "Routine, reward, and puzzle system for kids",
        "status": "Done",
        "path": "specs/luna-rituals.html",
    },
    {
        "name": "Helix7",
        "href": "specs/helix7.html",
        "description": "Voice-note-to-web-novel workflow",
        "status": "In progress",
        "path": "specs/helix7.html",
    },
]


def github_json(url: str):
    token = os.environ.get("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "portfolio-readme-metadata-updater",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = Request(url, headers=headers)
    with urlopen(req, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def latest_commit_for_path(path: str) -> tuple[str, str]:
    encoded_path = quote(path)
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits?path={encoded_path}&per_page=1"
    commits = github_json(url)
    if not commits:
        return "pending", "pending"
    commit = commits[0]
    sha = commit["sha"][:7]
    raw_date = commit["commit"]["committer"]["date"]
    dt = datetime.fromisoformat(raw_date.replace("Z", "+00:00")).astimezone(timezone.utc)
    return f"rev-{sha}", dt.strftime("%Y-%m-%d")


def build_table() -> str:
    rows = [
        START,
        '<div align="center">',
        "",
        "<table>",
        "  <thead>",
        "    <tr>",
        '      <th align="left">Project</th>',
        '      <th align="left">What it is</th>',
        '      <th align="left">Status</th>',
        '      <th align="left">Version</th>',
        '      <th align="left">Last updated</th>',
        "    </tr>",
        "  </thead>",
        "  <tbody>",
    ]

    for project in PROJECTS:
        try:
            version, updated = latest_commit_for_path(project["path"])
        except Exception as exc:  # noqa: BLE001 - keep README update resilient
            print(f"Could not read metadata for {project['name']}: {exc}")
            version, updated = "pending", "pending"

        rows.extend(
            [
                "    <tr>",
                f'      <td><a href="{project["href"]}"><strong>{project["name"]}</strong></a></td>',
                f'      <td>{project["description"]}</td>',
                f'      <td>{project["status"]}</td>',
                f'      <td><code>{version}</code></td>',
                f"      <td>{updated}</td>",
                "    </tr>",
            ]
        )

    rows.extend(
        [
            "  </tbody>",
            "</table>",
            "",
            "</div>",
            END,
        ]
    )
    return "\n".join(rows)


def main() -> None:
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit("README.md is missing FEATURED_BUILDS markers.")

    before = text.split(START, 1)[0]
    after = text.split(END, 1)[1]
    new_text = before + build_table() + after
    README.write_text(new_text, encoding="utf-8")


if __name__ == "__main__":
    main()
