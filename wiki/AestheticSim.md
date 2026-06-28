# AestheticSim

AestheticSim is a facial aesthetics consultation OS for medspas.

## Current paths

- App demo: `apps/aesthetic-sim.html`
- Spec page: `specs/aesthetic-sim.html`
- Thumbnail: `assets/aesthetic-sim-thumb.jpg`

## Product summary

AestheticSim helps turn a subjective medspa consultation into a structured visual plan.

It includes:

- Client intake wizard
- AI-style facial analysis
- Clinician review board
- Treatment plan editor
- Skincare plan
- Admin panel
- Downloadable consultation board

## Current design system

AestheticSim should stay visually distinct from the warm portfolio shell.

Use:

- Cool body background: `#F1F1F5`
- Zinc neutrals
- Violet accents
- Dark `zinc-950` headers
- OS-style cards and panels

Avoid:

- Warm beige product UI
- Portfolio neobrutalist styling inside the app

## Demo clients

Mock clients currently used for demos:

- Jasmine Carter — needs review
- Marcus Webb — approved; use this path to demo the downloadable board
- Renee Washington — analyzing; includes weight-loss support context
- Sofia Reyes — booked; shows the post-booking gate before intake unlocks

All clients are mock data.

## Key demo flows

### 1. Landing role selection

Show how a clinic, client, or admin enters the system.

### 2. Admin Panel

Admin config includes:

- Branding
- Clinic name and tagline
- Logo text / logo URL
- Disclaimer
- Integrations
- Booking/deposit configuration
- Board settings

### 3. Booked client gate

Clients with a booked state should first see booking confirmation, deposit receipt, and appointment date before intake starts.

### 4. Clinician board

The board should show the strongest visual proof: client list, analysis states, and facial mapping.

### 5. Downloadable board

Approved clients can generate a printable consultation board using browser print / Save as PDF.

The board should include:

- Clinic header
- Disclaimer
- Executive summary
- Facial mapping
- Aging analysis
- Skin quality
- Balancing opportunities
- Top ROI treatments
- Treatment phases
- Simulation gallery
- Cost forecast

## Thumbnail standard

Use `assets/aesthetic-sim-thumb.jpg` anywhere AestheticSim appears in a project card.

The thumbnail should show the consultation board with facial mapping dots, because that is the clearest money shot.
