# Thumbnails and Visuals

Every project needs a thumbnail. The portfolio should lead with proof, not placeholders.

## Display rule

On both the landing page and full portfolio page:

1. Show projects with real thumbnails or live previews first.
2. Move placeholder-only projects lower.
3. Keep placeholder cards only as temporary scaffolding.

## Thumbnail requirements

Each thumbnail should:

- Show the actual product or production output
- Use dummy or public-safe data
- Have useful alt text
- Be visually inspected before commit
- Be optimized for web size
- Fit the card aspect ratio cleanly

## Preferred thumbnail types

| Project type | Best thumbnail |
|---|---|
| App | Screenshot of the strongest workflow screen |
| Build log | Screenshot sequence or annotated process image |
| Creative system | Character sheet, storyboard frame, or production board |
| Fiction workflow | Voice note to outline to chapter visual |
| Interior/design tool | Before/after or generated render grid |
| Data/finance app | Sanitized dashboard with fake values |
| Kids app | Public-alias routine screen with no real details |

## Current thumbnail inventory

| Project | Current visual status | Next action |
|---|---|---|
| BonnetNoona | Embedded pitch preview | Keep first |
| AestheticSim | `assets/aesthetic-sim-thumb.jpg` | Wire everywhere |
| The Helix Class | Character concept visuals | Keep high in portfolio grid |
| Aurë / Accord | Placeholder | Capture app screen |
| Roommate Tracker | Placeholder | Create dummy-data dashboard screenshot |
| My Plate Planner | Placeholder | Create dummy-data meal plan screenshot |
| Helix7 | Placeholder | Create workflow/manuscript screenshot |
| Interior Render Studio | Placeholder | Capture render studio UI or output |
| Kids' Habit + Reward App | Placeholder / alias-sensitive | Capture public-alias screen only |

## File naming convention

Use this pattern:

```text
assets/<project-slug>-thumb.jpg
assets/<project-slug>-thumb.png
```

Examples:

```text
assets/aesthetic-sim-thumb.jpg
assets/aure-thumb.jpg
assets/interior-render-thumb.jpg
assets/plate-planner-thumb.jpg
assets/roommate-tracker-thumb.jpg
```

## HTML pattern

Use this card thumbnail pattern:

```html
<div class="thumb">
  <img src="assets/project-thumb.jpg" alt="Concise description of the actual product screenshot" loading="lazy" />
</div>
```

Avoid placeholder blocks like this except temporarily:

```html
<div class="thumb ph"><span class="big">PLACEHOLDER</span></div>
```

## Screenshot QA

Before committing screenshots:

- Check for private names
- Check browser chrome and visible tabs
- Check email/account leaks
- Check financial numbers
- Check child-related details
- Check medical/health details
- Confirm dummy data is obvious enough for public use
