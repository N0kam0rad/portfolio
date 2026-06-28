# Privacy and QA

Privacy is non-negotiable. This is a public portfolio, so every project must use safe public-facing names, dummy data, and sanitized screenshots.

## Hard privacy rules

- Do not publish real minor-identifying details.
- Use public aliases for child-facing projects and cast references.
- Use dummy data only for financial, household, health, medical, school, and family workflows.
- Do not include private account numbers, balances, addresses, school details, real routines, or real contact data except the public portfolio email.

## Public aliases

- BonnetNoona child cast member: `Mira`
- Kids' Habit + Reward App child user: `Luna`

## Blocked-string check before push

Before publishing, check the public site files for blocked strings. Use a case-insensitive search across HTML, CSS, JS, Markdown, and text files.

```bash
grep -RniE "blocked-string-1|blocked-string-2|blocked-string-3" . \
  --include='*.html' \
  --include='*.css' \
  --include='*.js' \
  --include='*.md' \
  --include='*.txt'
```

Keep the actual private strings out of this wiki page. Store them only in private handoff notes or local checks.

## Image QA

Text baked into images cannot be caught by grep.

Before adding any image to `assets/`:

1. Open the image.
2. Check visible names, addresses, emails, dates, schools, balances, and health details.
3. Confirm the screenshot uses dummy data.
4. Confirm no browser tabs or bookmarks leak private info.
5. Confirm alt text describes the image without private details.

## Project-specific privacy notes

### Roommate Tracker

Use dummy names, dummy balances, dummy payment history, and fake rent numbers.

### My Plate Planner

Use generic diet constraints and dummy pantry data. Do not publish medication details, private health context, real grocery history, or real family data.

### Kids' Habit + Reward App

Use public alias `Luna`. Do not publish real name, school, real routines, real rewards, real photos, or identifiable details.

### BonnetNoona

Use public alias `Mira` for the child cast member. Keep the privacy note visible in the build-log post.

### AestheticSim

Use mock clients only. Photos should be stock or generated images, not private client photos.

## QA checklist before publishing

- [ ] No blocked private strings in public text files
- [ ] All screenshots visually inspected
- [ ] All financial and health examples use dummy data
- [ ] All child references use public aliases
- [ ] All images have useful alt text
- [ ] No client-side gate is described as real security
- [ ] Project cards with thumbnails display before placeholder cards
- [ ] Links work from GitHub Pages root
