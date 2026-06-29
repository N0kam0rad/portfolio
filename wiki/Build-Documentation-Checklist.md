# Build Documentation Checklist

Each build needs enough documentation to support the portfolio card, the spec page, the blog post, and future UI/product work.

## Required documentation for every build

### 1. Product brief

- Project name
- One-sentence description
- Status: Prototype, In progress, Draft, or In production
- Problem statement
- Target user / ICP
- Main use case
- Current state
- Next build step

### 2. Product spec

- What it is
- Who it is for
- Core features
- User workflow
- Data model or content model, if relevant
- Design principles
- Privacy constraints
- Monetization idea
- Known limitations
- Future roadmap

### 3. Blog/case-study post

Must include:

- What it is
- Why I built it
- How I built it
- ICP / target user
- Market fit
- Sales pitch
- Screenshots and workflow visuals
- Update log
- CTA to reach out

### 4. Asset folder

Recommended path:

```text
assets/<project-slug>/
```

Required assets:

- `thumb` — portfolio card thumbnail
- `hero` — blog hero image
- `screenshots/` — product screenshots or mockups
- `workflow/` — workflow diagrams, prompt flow, architecture, or process images
- `icp/` — ICP or persona notes/visuals
- `sales/` — pitch slide, one-pager, or positioning notes

### 5. Screenshots / mockups

Minimum visual set:

- 1 portfolio thumbnail
- 1 hero image
- 3 workflow screenshots or mockups
- 1 key screen / money shot
- 1 process or architecture visual

For draft projects, use clearly labeled mockups or process visuals. Do not imply the UI is usable if it is not.

### 6. Workflow documentation

Include:

- Entry point
- User steps
- Main decision points
- Output/result
- Failure states
- What still needs to be built

### 7. ICP documentation

Include:

- Primary user
- Primary buyer, if different
- User pain
- Buying trigger
- Success metric
- Existing alternatives
- Why this product is different

### 8. Sales documentation

Include:

- One-sentence pitch
- 30-second pitch
- Problem/value bullets
- Demo story
- Pricing or packaging hypothesis
- Objection handling notes
- CTA

### 9. Update log

Every build should have a dated update log.

Use this format:

| Date | Update | Why it changed |
|---|---|---|
| YYYY-MM-DD | Specific change | Reason or learning |

### 10. Privacy and QA notes

Include:

- Dummy-data confirmation
- Private-name check
- Image inspection confirmation
- Links checked
- Status label checked
- App/demo actually usable, if marked Prototype

## Project-specific documentation needs

### AestheticSim

- Consultation-board screenshots
- Admin panel screenshots
- Client gate screenshots
- Treatment-plan workflow
- Medspa ICP notes
- Sales pitch for medspa owners or injectors
- Disclaimer/privacy notes

### BonnetNoona

- Cast sheet
- Relationship map
- Character reference assets
- Expression packs
- Storyboard frames
- Production workflow
- Episode/update log
- Pitch assets

### Aurë / Accord

- Fragrance wardrobe UI mockups
- Galaxy/orbit workflow
- Wear log flow
- Recommendation flow
- Fragrance-user ICP
- Monetization hypothesis

### Interior Render Studio

- Before/after mockups
- Style-selection workflow
- Render-output examples
- Home decor ICP
- Pricing/lead-gen hypothesis

### Roommate Tracker

- Dummy-data dashboard
- Payment flow
- Balance history
- Privacy note: no real financial data
- Household ICP
- Use-case examples

### My Plate Planner

- Dummy meal-plan screens
- Pantry/fridge workflow
- Protein tracking view
- Privacy note: no personal health/medication context
- User persona and diet constraints

### Helix7

- Voice-note workflow
- Outline-to-chapter visual
- Draft reader UI
- Story bible notes
- Update log by chapter/build pass

### The Helix Class

- Character sheets
- Webtoon reader mockup
- Worldbuilding notes
- Episode structure
- Visual style guide

### Kids' Habit + Reward App

- Public alias only
- Routine dashboard mockups
- Reward flow
- Parent/admin flow
- Privacy note: no real minor name, routines, school, or photos
