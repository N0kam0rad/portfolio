# Visitor Analytics Plan

**Created:** 2026-06-29  
**Portfolio:** https://n0kam0rad.github.io/portfolio/

---

## Goal

Understand which products visitors care about, which CTAs convert, and where people drop off — without collecting personal data or needing a cookie banner.

The portfolio has no analytics today. This plan defines what to track, how to name events, and how to install the recommended tool on GitHub Pages.

---

## Recommended Tool: Plausible Analytics

**Why Plausible:**
- Privacy-first: no cookies, no personal data, GDPR-compliant out of the box — no consent banner needed
- Works on GitHub Pages (just a `<script>` tag)
- Page views, referrers, and custom events all included in the free trial; paid plan is ~$9/month
- Clean single-dashboard view — no data model to learn
- Outbound click tracking is built-in (automatic on any `<a target="_blank">`)

**Alternatives considered:**
- Umami — self-hosted option (needs a server, not GitHub Pages-friendly without a separate host)
- Cloudflare Web Analytics — free but requires Cloudflare-proxied domain
- Google Analytics 4 — overkill for this use case; requires a consent banner in most regions

**Setup steps:**
1. Create a free account at plausible.io
2. Add your site: `n0kam0rad.github.io` with base path `/portfolio`
3. Copy your snippet — it looks like:
   ```html
   <script defer data-domain="n0kam0rad.github.io" src="https://plausible.io/js/script.tagged-events.js"></script>
   ```
   Use the `tagged-events` variant to enable custom event tracking.
4. Add the snippet to the `<head>` of every HTML page: `index.html`, `portfolio.html`, `blog.html`, `tools.html`, `ideas.html`, `contact.html`
5. For spec pages and post pages, add it to each file in `specs/` and `posts/`
6. Verify in the Plausible dashboard that page views appear

**Placeholder — paste your Plausible site ID here:**
```
YOUR_PLAUSIBLE_SITE_ID = n0kam0rad.github.io
```
The snippet goes in `<head>`, before `</head>`, on every page.

---

## What We Should Track

### Page views (automatic with Plausible)
- All pages — Plausible tracks these out of the box with the script installed

### Outbound clicks (automatic with `tagged-events` script)
- Plausible auto-tracks all `<a target="_blank">` clicks as "Outbound Link: Click" events
- This covers: TikTok, Instagram, GitHub, LinkedIn, Tiiny sites, aestheticsim.tiiny.site

### Custom events (manual, added via `class="plausible-event-name=..."` or JS)

#### Global events

| Event Name | Trigger | Where |
|------------|---------|-------|
| `portfolio_nav_click` | Drawer or top nav link clicked | All pages |
| `portfolio_email_cta_click` | Email link clicked in footer/contact | All pages |
| `portfolio_gate_opened` | Gate modal appears | `index.html`, `portfolio.html` |
| `portfolio_gate_unlocked` | User clicks "I followed" or submits email | `index.html`, `portfolio.html` |
| `portfolio_resume_click` | Resume link clicked (if added later) | Contact, about |

#### Per-product events

| Event Name | Trigger | Where |
|------------|---------|-------|
| `portfolio_product_card_click` | Product card in grid is clicked (or CTA inside clicked) | `portfolio.html`, `index.html` |
| `portfolio_demo_click` | Lock-btn prototype opened | All pages with lock-btn |
| `portfolio_spec_click` | "Read the spec →" clicked | `portfolio.html` |
| `portfolio_case_study_click` | "Read the build →" or "Read the build log →" clicked | `portfolio.html`, `blog.html` |
| `portfolio_external_app_click` | Link to external app (Tiiny, etc.) clicked | `portfolio.html`, `blog.html` |

#### Specific product events

| Event Name | Trigger |
|------------|---------|
| `aestheticsim_demo_click` | AestheticSim prototype unlocked |
| `aestheticsim_tiiny_click` | `aestheticsim.tiiny.site` external link clicked |
| `aestheticsim_spec_click` | AestheticSim spec page opened |
| `aestheticsim_buildlog_click` | AestheticSim build log link clicked |
| `aure_demo_click` | Aurë app unlocked |
| `aure_spec_click` | Aurë spec clicked |
| `bonnetnoona_pitch_click` | BonnetNoona pitch deck unlocked |
| `bonnetnoona_buildlog_click` | BonnetNoona build log clicked |
| `luna_demo_click` | Luna's Rituals app unlocked |
| `luna_spec_click` | Luna's Rituals spec clicked |
| `interior_render_spec_click` | Interior Render spec clicked |
| `roommate_tracker_spec_click` | Roommate Tracker spec clicked |
| `plate_planner_spec_click` | My Plate Planner spec clicked |
| `helix7_spec_click` | Helix7 spec clicked |
| `helix_class_buildlog_click` | Helix Class build log clicked |

---

## What We Should NOT Track

- Names, emails, or any personal identifiers
- IP addresses (Plausible does not store raw IPs — it aggregates anonymously)
- Exact user identity or session stitching
- Keystrokes or form contents
- Any data from the gate email form until a proper newsletter backend is set up
- Location beyond country-level (Plausible shows country by default — do not add fingerprinting)

---

## Event Naming Convention

Use `snake_case`. Format: `product_action` or `portfolio_action`.

```
portfolio_gate_opened
portfolio_gate_unlocked
portfolio_demo_click
portfolio_spec_click
portfolio_case_study_click
portfolio_external_app_click
portfolio_email_cta_click
aestheticsim_demo_click
aestheticsim_tiiny_click
luna_demo_click
bonnetnoona_pitch_click
```

**Properties to send with events (where Plausible custom props are enabled):**
- `product_name` — e.g. "AestheticSim", "Luna's Rituals"
- `product_status` — "Served", "Cooking", "Spark"
- `destination_url` — the target URL the user clicked to
- `source_page` — "portfolio", "home", "blog"
- `link_type` — "spec", "build_log", "demo", "external_app", "pitch"

---

## Product-Level Tracking Matrix

| Product | Track Demo | Track Spec | Track Blog | Track External App | Track Pitch |
|---------|-----------|------------|------------|-------------------|-------------|
| AestheticSim | ✅ | ✅ | ✅ | ✅ (Tiiny) | — |
| Luna's Rituals | ✅ | ✅ | when added | — | — |
| BonnetNoona | — | when added | ✅ | — | ✅ (Tiiny pitch) |
| Aurë | ✅ (UI preview) | ✅ | ✅ | — | — |
| Interior Render | — | ✅ | ✅ | — | — |
| Roommate Tracker | — | ✅ | ✅ | — | — |
| My Plate Planner | — | ✅ | ✅ | — | — |
| Helix Class | — | when added | ✅ | — | — |
| Helix7 | — | ✅ | ✅ | — | — |

---

## Privacy Notes

- Plausible does not use cookies and does not require a consent banner in any region
- No PII is collected — visitors are counted by aggregated metrics, not individual profiles
- The embedded Tiiny iframe (BonnetNoona pitch preview) fires its own analytics ping (`analytics.tiiny.site`) on page load — this is outside our control but is Tiiny's own tracker
- The gate email form on `index.html` does not currently POST emails to any server — it only unlocks the page. When a newsletter backend is added, it must comply with CAN-SPAM and GDPR: explicit opt-in, easy unsubscribe, no resale
- Roommate Tracker and My Plate Planner must continue to use dummy data only — never track user-submitted real data from these apps

---

## Implementation Steps

### Step 1: Create Plausible account
- Go to plausible.io → Start Free Trial
- Add site: `n0kam0rad.github.io`
- Note: Plausible supports sites on shared domains. Set the base path as `/portfolio` in the site settings.

### Step 2: Add base script to all pages
Add the following to `<head>` in each HTML file. Replace `YOUR_DOMAIN` with `n0kam0rad.github.io`:

```html
<script defer data-domain="YOUR_DOMAIN" src="https://plausible.io/js/script.tagged-events.js"></script>
```

Files to update:
- `index.html`
- `portfolio.html`
- `blog.html`
- `tools.html`
- `ideas.html`
- `contact.html`
- All files in `specs/`
- All files in `posts/`

### Step 3: Tag gate events with JS
In `index.html` and `portfolio.html`, add Plausible event calls to the gate logic:

```js
// When gate opens
function openGate(app) {
  if (typeof plausible !== 'undefined') plausible('portfolio_gate_opened', { props: { product_name: app || 'unknown' } });
  // ... existing code
}

// When gate is unlocked
function unlock() {
  if (typeof plausible !== 'undefined') plausible('portfolio_gate_unlocked', { props: { source_page: document.title } });
  // ... existing code
}
```

### Step 4: Tag product CTAs
Add `class="plausible-event-name=aestheticsim_spec_click"` to specific links, or use JS:

```js
document.querySelectorAll('[data-track]').forEach(el => {
  el.addEventListener('click', () => {
    const ev = el.getAttribute('data-track');
    const props = el.dataset.trackProps ? JSON.parse(el.dataset.trackProps) : {};
    if (typeof plausible !== 'undefined') plausible(ev, { props });
  });
});
```

Then in HTML:
```html
<a class="lnk" href="specs/aesthetic-sim.html"
   data-track="portfolio_spec_click"
   data-track-props='{"product_name":"AestheticSim","link_type":"spec"}'>
  Read the spec →
</a>
```

### Step 5: Verify in dashboard
After pushing, open the Plausible dashboard and confirm:
- Page views appear for each page
- Outbound clicks fire when clicking TikTok/Instagram/GitHub/LinkedIn/Tiiny links
- Custom events appear after clicking spec/demo/build-log CTAs

---

## What a Successful Visit Looks Like Per Product

| Product | Success metric |
|---------|---------------|
| AestheticSim | Visitor clicks demo OR spec OR Tiiny link |
| Luna's Rituals | Visitor clicks demo or spec |
| BonnetNoona | Visitor clicks pitch unlock or build log |
| Aurë / Accord | Visitor clicks spec (no demo yet) |
| Any "Cooking" product | Visitor clicks spec or build log — shows interest |
| Contact page | Visitor clicks email CTA or submits contact form |

---

*This plan requires a Plausible account and domain registration before any script goes live. No account IDs have been hardcoded in portfolio HTML — paste your site ID when the account is created.*
