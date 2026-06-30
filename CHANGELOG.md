# Changelog

All notable changes to this portfolio site are documented here, grouped by date (newest first). This is a personal portfolio of multiple small apps and case studies rather than a single versioned product, so entries are dated rather than semver-tagged. Routine automated commits (README metadata refreshes) are omitted.

## 2026-06-30 — AestheticSim: clinical grounding + 3D simulation

### Added
- **Clinically-grounded dosing**: a `CLINICAL_REFERENCE` source-of-truth for Botox units per zone, HA filler mL per region, Sculptra vials, onset, and longevity — all cited to published research. Provider plan rows now show real units (U / mL / vials) instead of placeholder numbers.
- **Depth-aware 3D facial simulation**: the on-photo treatment simulator now uses real anatomic injection zones, 3D landmark depth (z-axis) for the warp, and a visible 3D face-mesh/injection-point overlay (MediaPipe `FACE_LANDMARKS_TESSELATION`).
- **Treatment-correct physics**: filler adds volume, neuromodulator lifts/softens lines (no volume), biostimulator is gradual, energy treatments add glow — simulated differently per treatment kind instead of one generic effect.
- **Contour map mode**: a VECTRA XT–inspired "Gray Mode" + volume-difference view that desaturates the photo and shades simulated change (warm = added volume, cool = lift/displacement).
- **Provider simulation kill switch**: a clinic-level toggle (Admin → Board Settings) that hides the entire facial-balancing simulation everywhere — for jurisdictions that regulate simulated before/afters — while leaving the skin-analysis and treatment plan untouched.
- **Dose-visibility toggle**: providers always see exact doses; a separate toggle controls whether clients see exact units/mL or just treatment names.
- **Personalized simulation**: treatment suggestions are now derived from the client's actual scan scores pre-approval, and reflect the provider's approved plan post-approval.
- **Heatmap restored** on the client dashboard skin-analysis card, with tappable concern chips.
- Cited research write-up ("Clinical grounding & research") added to the AestheticSim build log — units per area, why simulation physics differ by treatment, the 3D-imaging precedent (Crisalix, Canfield VECTRA), vascular safety zones, and an honest "evaluated but not integrated" section on FLAME and KeenTools (license/multi-photo constraints ruled them out for a single-photo, client-side app).

## 2026-06-29 — AestheticSim: real on-device scan + unified workflow

### Added
- Real on-device skin analysis (MediaPipe Face Landmarker) replacing the mocked "analyzing" state — 7 skin-concern scores, a tappable heatmap overlay, and an identity-preserving before/after simulation built from the actual scan.
- Unified the workflow end to end: the 4-photo intake now runs the real scan, routes the client into the provider's review queue with an auto-generated starter plan, and the approved result appears back on the client's dashboard.
- Provider treatment customization: Injectables/Facials/Both filter, a treatment-library dropdown, a custom-treatment form (requires a procedure description + benefits), and a recommended-products list with sponsored/partner badges.
- "Not sure / I don't know" added as a valid answer on every intake question.
- QA pass across the portfolio: naming consistency and identity standardization.

## 2026-06-28 — AestheticSim polish, build logs, portfolio branding

### Added
- Build logs published for every app in the portfolio (AestheticSim, Aurë, Accord, Interior Render Studio, Roommate Tracker, Plate Planner, Helix7, The Helix Class).
- Branded status labels (Served / Cooking / On deck / Spark) applied across the portfolio grid, sorted by completion state.
- Demo video assets and an autoplay portfolio-card preview for AestheticSim.

## 2026-06-27 — AestheticSim ships its first usable shell; portfolio wiki + thumbnails

### Added
- AestheticSim: full UI shell shipped — intake wizard, clinician consultation board, admin panel with booking gate, and a downloadable PDF consultation board.
- The Helix Class webtoon project card added (coming soon).
- Portfolio wiki: repo map, project roster, operating manual, privacy/QA, thumbnails, and blog-standards pages.
- Thumbnail-first project cards replaced the old grid; dynamic README metadata workflow added.
- BonnetNoona: cast grid rebuilt from locked character references; old contact sheet removed (had a real child's name baked in — privacy fix).

### Fixed
- Babel parse break from an unescaped apostrophe; `draft` `useState` ordering bug in `ClinicianApp`; `ConsultationBoard` crashing on first render without a plan fallback.

## 2026-06-25 – 2026-06-26 — Site hero + BonnetNoona pitch

### Added
- Interactive "Angela-Anaconda brain collage" homepage hero with clickable post-it hotspots, springing open-on-hover animation, and a transparent full-viewport treatment.
- Live BonnetNoona pitch-deck link and iframe preview card.
- Tamara-head custom cursor, peering-eyes drawer trigger, glass nav.

## 2026-06-23 – 2026-06-24 — Initial site

### Added
- Initial portfolio site commit and asset upload.
- Motion pass on the homepage (GSAP, smooth scroll, custom cursor, marquee).
- First BonnetNoona build log and reusable build-log template.
