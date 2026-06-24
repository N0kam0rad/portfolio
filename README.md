# Tamara Richards — (almost)CEO

A portfolio of apps and passion projects shipped with AI — plus a build log of the exact tools, prompts, and skills behind each one. Built for the **Google Flow Sessions** cohort and as a living home for everything I make.

🔗 **Live site:** _(add your GitHub Pages URL here once published — see below)_

---

## The idea

I have more ideas than hours. AI is the bridge between my ADHD brain and a finished product — so the idea that wins the day actually gets built. This site collects them, and the blog shows exactly *how* each one was made: the LLM, the tool, the skill, the prompt, the how-to.

> Idea → AI → shipped.

## What's here

- **Home (`index.html`)** — hero, the "how I work" engine, project cards, a "Lab" wall of unbuilt ideas, the build log, and contact.
- **Projects:** BonnetNoona (live, with shots), plus AI Analysis, Rewards, and Aura / Accord as "in the lab" cards ready to be filled in.
- **Build log (`posts/`)** — one full post (the BonnetNoona AI-cast how-to) and a reusable template.

## Design

Bold, color-blocked, expressive — inspired by award-winning personality portfolios (think *Besharm*). Warm paper canvas, a signature red, oversized type, a scrolling idea-ticker, hover-tilt project cards, and a draggable sticker wall. Fonts: Bricolage Grotesque + Fraunces (italic accents) + Inter.

## Add a new blog post (no coding needed)

1. Duplicate `posts/_TEMPLATE.html` and rename it (e.g. `posts/building-the-rewards-app.html`).
2. Open it and fill in the numbered spots: title, project name, tags, and the body. The building blocks (headings, callout, prompt block, image grid, end card) are all there — copy what you need.
3. Drop any screenshots into `assets/` and point the `<img src="../assets/...">` tags at them.
4. On `index.html`, swap one of the "Coming soon" stubs in the **Build log** section for a link to your new post.

## Folder structure

```
Portfolio/
├── index.html        # the site (single file, no build step)
├── assets/           # optimized images
├── posts/
│   ├── how-i-built-a-consistent-ai-cast.html
│   └── _TEMPLATE.html   # copy this for new posts
├── .nojekyll
└── README.md
```

## Publish on GitHub Pages (free)

1. Create a new public repo on GitHub (e.g. `tamara-portfolio`).
2. Upload this folder's contents, or push from the terminal:

```bash
cd Portfolio
rm -rf .git          # clear any partial repo first
git init
git add .
git commit -m "Tamara Richards portfolio"
git branch -M main
git remote add origin https://github.com/<your-username>/tamara-portfolio.git
git push -u origin main
```

3. In the repo: **Settings → Pages → Source: Deploy from a branch**, pick `main` / root, **Save**.
4. Live at `https://<your-username>.github.io/tamara-portfolio/` within a minute or two.

---

_Original work by Tamara Richards. Ideas, shipped with AI._
