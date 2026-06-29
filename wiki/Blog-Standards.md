# Blog Standards

Build logs should read like compact product case studies: clear enough for a hiring manager, useful enough for another builder, and persuasive enough for a potential collaborator or buyer.

Every build post should answer:

1. What is it?
2. Why did I build it?
3. How did I build it?
4. Who is it for?
5. Where does it fit in the market?
6. How would I sell or pitch it?
7. What changed over time?
8. What should someone do after reading?

## Standard blog format

Use this structure for every project/build post.

```markdown
# [Project Name]: [plain-English outcome]

Date started: YYYY-MM-DD
Last updated: YYYY-MM-DD
Status: Prototype | In progress | Draft | In production
Related links: Spec | Demo/prototype | Repo/assets | Build log index

## 1. What it is

One clear paragraph explaining the product, tool, creative system, or workflow.

Include:
- Product category
- Who uses it
- What it helps them do
- Current status, honestly stated

## 2. Why I built it

Explain the personal, professional, creative, or market problem that triggered the build.

Include:
- The pain point
- Why existing options were not enough
- Why this problem was worth prototyping
- What I wanted to prove

## 3. Who it is for

Define the user or buyer.

Include:
- Primary ICP
- Secondary ICP
- User job-to-be-done
- Buying trigger
- What success looks like for them

## 4. How I built it

Show the actual process.

Include:
- Tools used
- AI workflow
- Prompting strategy
- Manual product decisions
- Data/model/design assumptions
- What I rejected or changed

## 5. Product walkthrough

Use screenshots and captions to walk through the experience.

Include:
- Entry point
- Core workflow
- Key screen or money shot
- Output/result
- Edge cases or future states

## 6. Market fit

Explain why this could matter beyond the portfolio.

Include:
- Market category
- Competitors or alternatives
- Why now
- User urgency
- Differentiation
- Monetization angle

## 7. Sales pitch

Write the direct buyer-facing pitch.

Include:
- One-sentence pitch
- Problem statement
- Value proposition
- Why it is better/different
- Example use case
- Pricing or packaging hypothesis, if relevant

## 8. What changed / update log

Keep a dated build trail.

Use this format:

| Date | Update | Why it changed |
|---|---|---|
| YYYY-MM-DD | Added/changed/fixed something specific | Explain the reason |

## 9. What I learned

Explain the product, AI, UX, technical, or creative lesson.

## 10. What I would build next

List the next 3-5 build steps.

## 11. Call to action

End every post with a direct invitation:

Interested in building something like this, collaborating, or seeing the prototype? Reach out to me at `richards.tlynn@gmail.com`.
```

## Required assets for each blog post

Every build blog needs a folder of supporting assets. Text alone is not enough.

### Visual assets

- Hero thumbnail for the blog index
- At least 3 screenshots or mockups
- One workflow/process image
- One final-state or current-state image
- Optional before/after image
- Optional short demo clip or GIF

### Product assets

- Product spec link
- Demo/prototype link when usable
- Feature list
- User flow or workflow map
- Status label: Prototype, In progress, Draft, or In production
- Known limitations
- Next-build list

### Market and sales assets

- ICP notes
- Buyer/user persona
- Jobs-to-be-done
- Competitor/alternative notes
- Market-fit hypothesis
- Sales pitch paragraph
- Pricing/packaging hypothesis, if relevant

### Build/process assets

- Tool stack
- Prompt snippets or prompt strategy
- Architecture notes
- Data model notes, if relevant
- Design system notes
- QA notes
- Privacy review notes
- Dated update log

## Screenshot requirements

Every build-log post should include relevant screenshots.

Use screenshots to show:

- Before / after states
- UI flows
- Prompt outputs
- Reference images
- Production boards
- Error or drift examples
- Final or current state
- Workflow maps
- ICP or persona snapshots, when relevant

Do not rely on text only when the post is about visual or product work.

## Screenshot captions

Captions should explain why the screenshot matters.

Good:

> The final consultation board became the card thumbnail because it shows the core value in one frame: facial mapping, analysis, and treatment planning.

Weak:

> Screenshot of app.

## Voice

Write like a builder explaining the recipe and a product strategist explaining the market.

Use:

- Specific nouns
- Real tradeoffs
- Clear steps
- Honest lessons
- Plain-English market framing
- Warm confidence

Avoid:

- Generic AI hype
- Fake certainty
- Empty founder-speak
- Calling a project shipped when it is not usable
- Posting screenshots without context
- Hiding the human product judgment behind prompts

## Blog QA checklist

- [ ] Includes date started and last updated
- [ ] Uses honest status label
- [ ] Explains what it is
- [ ] Explains why I built it
- [ ] Explains how I built it
- [ ] Defines ICP / user / buyer
- [ ] Includes market-fit section
- [ ] Includes sales pitch section
- [ ] Includes screenshots, mockups, or workflow visuals
- [ ] Includes dated update log
- [ ] Explains what AI helped with
- [ ] Explains what human judgment controlled
- [ ] Includes limitations / not-yet-built notes
- [ ] Includes next-build steps
- [ ] Has privacy-safe images and copy
- [ ] Links to related spec or demo when available
- [ ] Ends with CTA to reach out at `richards.tlynn@gmail.com`
