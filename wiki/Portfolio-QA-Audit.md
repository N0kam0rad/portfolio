# Portfolio QA Audit

**Audit date:** 2026-06-29  
**Auditor:** Claude Code (automated Playwright crawl + source review)  
**Site:** https://n0kam0rad.github.io/portfolio/  
**Related product audited:** https://aestheticsim.tiiny.site/

---

## Executive Summary

The portfolio is structurally sound and passes all core routes cleanly. No JS errors on the main pages. The brand voice and visual system are consistent across Home, Portfolio, Tools, Ideas, and Contact. However there are two P0/P1 issues that hurt the visitor experience: a confirmed 404 build log link for the top product (AestheticSim), and a complete absence of Luna's Rituals from the portfolio despite it having a working app and product spec. The live external version of AestheticSim (aestheticsim.tiiny.site) is also not linked from anywhere in the portfolio. There is currently no analytics instrumentation of any kind.

---

## Critical Issues

| # | Issue | Priority | Pages Affected |
|---|-------|----------|----------------|
| 1 | `posts/aestheticsim-build-log.html` returns 404 | P0 | `portfolio.html`, `blog.html` |
| 2 | `aestheticsim.tiiny.site` (live external app) not linked anywhere | P0 | `portfolio.html` |
| 3 | Luna's Rituals missing from portfolio entirely (has working app + spec) | P1 | `portfolio.html`, `index.html` |
| 4 | `blog.html` uses completely different nav and footer from all other pages | P1 | `blog.html` |
| 5 | No portfolio analytics of any kind | P1 | All pages |

---

## Dead Links / Broken Routes

| Source Page | Clicked Element | Expected | Actual | Severity |
|-------------|----------------|----------|--------|----------|
| `portfolio.html` | "Read the build →" on AestheticSim card | Build log page | **404 GitHub Pages** | P0 |
| `blog.html` | "Read the build →" on AestheticSim card | Build log page | **404 GitHub Pages** | P0 |
| `posts/aure-build-log.html` | `<link rel="stylesheet" href="../post.css"/>` | Stylesheet | **404 (not fatal — page has inline styles)** | P2 |

All other checked routes resolve cleanly:
- `index.html` ✅
- `portfolio.html` ✅
- `blog.html` ✅
- `tools.html` ✅
- `ideas.html` ✅
- `contact.html` ✅
- `specs/aesthetic-sim.html` ✅
- `specs/aure.html` ✅
- `specs/accord.html` ✅
- `specs/luna-rituals.html` ✅ (exists but product missing from portfolio)
- `specs/helix7.html` ✅
- `specs/interior-render.html` ✅
- `specs/plate-planner.html` ✅
- `specs/roommate-tracker.html` ✅
- `apps/aesthetic-sim.html` ✅
- `apps/aure.html` ✅
- `apps/luna-rituals.html` ✅ (exists but product missing from portfolio)
- `apps/bonnetnoona.html` ✅
- `posts/how-i-built-a-consistent-ai-cast.html` ✅
- `aestheticsim.tiiny.site` ✅ (live, but not linked from portfolio)

---

## Product Workflow Findings

### AestheticSim
- Card clearly communicates what the product is. Status "Served" is accurate.
- The "Read the build →" link is a confirmed 404. Visitors who click it hit a GitHub Pages error page — this is the top product on the portfolio.
- The gated app link (`apps/aesthetic-sim.html`) works.
- The external Tiiny site (`https://aestheticsim.tiiny.site/`) is live and unlocked but **not referenced anywhere** in the portfolio. Visitors never see it.
- Spec page exists and is linked. Build log placeholder created as part of this audit.

### Luna's Rituals
- Has a working app (`apps/luna-rituals.html`) with title "Luna's Rituals ✨".
- Has a product spec (`specs/luna-rituals.html`) titled "Kids' Habit + Reward App".
- **Completely absent from both `portfolio.html` and `index.html`.**
- By the site's own rule ("Finished or more complete products appear first"), this product should be in the Served section alongside AestheticSim.
- Privacy is maintained — "Luna" is the approved public alias; the child's real name does not appear in any portfolio file.

### BonnetNoona
- Has a working build log post ✅
- Has a gated pitch deck link ✅
- **No product spec page** (no `specs/bonnetnoona.html` exists)
- The card is clear on status (Cooking). Visitor knows what it is.

### Aurë / Accord
- Both specs exist ✅
- Build logs exist ✅
- No usable demo yet — card correctly says "Cooking"
- The lock-btn on `index.html` says "🔒 UI cooking" which is ambiguous — sounds like the UI is still being built (true), but a visitor may not understand they could unlock it

### The Helix Class
- Has Higgsfield character images in the thumbnail ✅
- Status "Cooking" is accurate
- Card links to `specs/helix7.html` as "Related system →" — this is Helix7's spec, not Helix Class's own. Helix Class has no spec page yet.
- Build log exists ✅

### Helix7
- Has a build log ✅
- Has a spec ✅
- Status "Spark" is accurate — no demo yet

### Interior Render Studio
- Spec exists ✅
- Build log exists ✅ (linked from `blog.html` but NOT from the portfolio card footer)
- No demo — "Cooking" is accurate

### Roommate Tracker
- Spec exists ✅
- Build log exists ✅ (linked from `blog.html` but NOT from the portfolio card footer)
- No demo — "Cooking" is accurate

### My Plate Planner
- Spec exists ✅
- Build log exists ✅ (linked from `blog.html` but NOT from the portfolio card footer)
- No demo — "Cooking" is accurate

---

## Visual QA Findings

### Desktop (1440px)
- Home hero renders cleanly. Brain image loads. Post-it tabs animate.
- Portfolio page: AestheticSim card has full thumbnail image. Cooking cards use abstract visual grids — clear and consistent.
- Marquee scrolls on both home and portfolio pages.
- Status badge sizes consistent across Served/Cooking/Spark cards.
- Footer links all present and formatted.

### Desktop (1024px)
- Not captured separately; behavior is equivalent to 1440px (max-width caps at 1180px).

### Mobile (390px)
- Home: hero stack collapses to single column, brain image centered. CTA row wraps cleanly. Marquee works.
- Portfolio: cards stack to single column. Thumbnail images maintain aspect ratio. Cooking mini-cards shrink predictably.
- Status badges remain readable.

### Observations
- The embedded Tiiny iframe in BonnetNoona and home page preview loads fine but fires a `POST analytics.tiiny.site/api/event` on page load — this is Tiiny's own tracker, not the portfolio's, and is outside our control.
- `blog.html` visually matches the portfolio color palette but uses a completely different nav structure (no hamburger, no drawer, no social links, no chip) and a plain `<footer>` text line. A visitor arriving on `blog.html` from Google would not see the full site navigation.

---

## Product Documentation Matrix

| Product | Status | Thumbnail | App/Demo | Spec | Blog/Log | Screenshots | Workflow Docs | ICP Docs | Sales Pitch | Update Log | QA/Privacy | In Portfolio | Priority |
|---------|--------|-----------|----------|------|----------|-------------|---------------|----------|-------------|------------|------------|--------------|----------|
| AestheticSim | Served | ✅ | ✅ gated | ✅ | ⚠️ stub | ✅ video | ❌ | ❌ | ❌ | ❌ | ✅ wiki | ✅ | P1 fill |
| Luna's Rituals | Served | ❌ | ✅ gated | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ wiki | ❌ **missing** | P1 add |
| BonnetNoona | Cooking | ❌ iframe | ✅ pitch | ❌ | ✅ | partial | partial | ❌ | ✅ pitch deck | ❌ | ✅ wiki | ✅ | P2 |
| Aurë | Cooking | ❌ visual | ❌ UI next | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | P2 |
| Accord | Cooking | ❌ visual | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ (with Aurë) | P2 |
| Helix Class | Cooking | ✅ chars | ❌ | ❌ own spec | ✅ | partial | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | P2 |
| Interior Render | Cooking | ❌ visual | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | P2 |
| Roommate Tracker | Cooking | ❌ visual | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ needs note | ✅ | P2 |
| My Plate Planner | Cooking | ❌ visual | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ needs note | ✅ | P2 |
| Helix7 | Spark | ❌ visual | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | P3 |

---

## AestheticSim Findings

**Live status:** The product exists in two separate deployment locations:
1. `https://n0kam0rad.github.io/portfolio/apps/aesthetic-sim.html` — gated behind the follow/unlock modal ✅ live
2. `https://aestheticsim.tiiny.site/` — **unlocked, live, and not linked from the portfolio**

**Portfolio representation:**
- Present in the Served section ✅
- Thumbnail `assets/aesthetic-sim-thumb.jpg` displays correctly ✅
- Status "Served" is accurate ✅
- Spec link (`specs/aesthetic-sim.html`) works ✅
- Build log link (`posts/aestheticsim-build-log.html`) was 404 — **stub created as part of this audit** ✅ fixed
- The Tiiny external URL was not linked — **added to card as part of this audit** ✅ fixed
- The wiki has strong product documentation (demo flows, client profiles, design system rules)
- No ICP document, no sales pitch document, no update log

**What AestheticSim still needs (manual content):**
- A real build log post (the stub is a placeholder)
- Screenshots from the consultation board
- An ICP document (medspas, aesthetic clinics)
- A one-page sales/pitch PDF or page

---

## Recommended Fix Plan

### P0 — Fix immediately (broken visitor experience)

| Fix | File(s) | Notes |
|-----|---------|-------|
| ~~Create `posts/aestheticsim-build-log.html` stub~~ | ✅ done | Placeholder with link to spec and app |
| ~~Add Tiiny external link to AestheticSim card~~ | ✅ done | Added to `portfolio.html` card footer |

### P1 — Fix soon (significant gaps)

| Fix | File(s) | Notes |
|-----|---------|-------|
| ~~Add Luna's Rituals card to Served section~~ | ✅ done | Added to `portfolio.html` |
| Update `blog.html` nav to match site-wide drawer nav | `blog.html` | Requires adding full drawer CSS + HTML + JS — non-trivial, schedule separately |
| Add portfolio analytics (Plausible recommended) | All pages | Needs account setup — see `Visitor-Analytics-Plan.md` |

### P2 — Polish (consistency + completeness)

| Fix | File(s) | Notes |
|-----|---------|-------|
| ~~Add `noreferrer` to all external `rel="noopener"` links~~ | ✅ done | `portfolio.html`, `index.html` |
| ~~Remove ghost `../post.css` reference from `aure-build-log.html`~~ | ✅ done | Inline styles handle the page; ghost link was a 404 |
| Add build log links to Cooking cards in `portfolio.html` | `portfolio.html` | Interior Render, Roommate Tracker, My Plate Planner card footers |
| Create a real spec page for Helix Class | `specs/helix-class.html` | Separate from Helix7 |
| Create a spec page for BonnetNoona | `specs/bonnetnoona.html` | Pitch doc exists; needs spec format |
| Clarify Aurë lock-btn label ("🔒 UI cooking" → "🔒 UI preview") | `index.html` | Minor copy |
| Add privacy/dummy-data badges to Roommate Tracker and Plate Planner cards | `portfolio.html` | Reinforce that no real data is used |

### P3 — Nice to have (content depth)

| Fix | Content needed |
|-----|---------------|
| AestheticSim real build log | Write and publish `posts/aestheticsim-build-log.html` |
| Luna's Rituals build log | Create `posts/luna-rituals-build-log.html` |
| Luna's Rituals screenshot/thumbnail | Add a real screenshot to `assets/` |
| ICP documents for AestheticSim, Aurë, BonnetNoona | Product strategy docs |
| Sales pitch pages for AestheticSim and Aurë | Investor/partner-facing |
| Update logs per product | Version/changelog tracking |

---

## Proposed Implementation Steps

1. ✅ Create `posts/aestheticsim-build-log.html` placeholder
2. ✅ Fix `portfolio.html`: add Tiiny link to AestheticSim card
3. ✅ Fix `portfolio.html`: add Luna's Rituals card to Served section
4. ✅ Fix external link `rel` attributes across `portfolio.html` and `index.html`
5. ✅ Fix `posts/aure-build-log.html`: remove ghost post.css reference
6. **Manual next:** Update `blog.html` to use the full site drawer nav
7. **Manual next:** Set up Plausible analytics (see `Visitor-Analytics-Plan.md`)
8. **Manual next:** Write the real AestheticSim build log post
9. **Manual next:** Add screenshot/thumbnail for Luna's Rituals
10. **Manual next:** Add blog log links to Interior Render, Roommate Tracker, Plate Planner cards in `portfolio.html`

---

## Visitor Analytics Findings

### Current state
- **No analytics installed.** There is no Google Analytics, Plausible, Umami, Fathom, or any other tracking script on any portfolio page.
- The only analytics ping observed during the Playwright crawl was `POST analytics.tiiny.site/api/event` — this is Tiiny.site's own tracker firing from the embedded BonnetNoona pitch deck iframe. It is not controlled by this portfolio.
- The gate email form on `index.html` collects email addresses client-side but does not POST them to any backend — the submit handler only calls `unlock()`. Email capture is not functional yet.

### What is not trackable today
- Page views
- Which products visitors click
- Which demos/specs/build logs are opened
- CTA conversion (how many visitors click "Work with me")
- Gate conversion (how many unlock the prototype)
- External link clicks (Tiiny, TikTok, Instagram, GitHub, LinkedIn)

### Recommended tool
**Plausible Analytics** — see `Visitor-Analytics-Plan.md` for the full implementation plan.

### Implementation priority
**P1** — install analytics before the next content push so engagement data starts accumulating.

---

*Audit conducted 2026-06-29. Re-run Playwright crawl after any major content push to catch new dead links.*
