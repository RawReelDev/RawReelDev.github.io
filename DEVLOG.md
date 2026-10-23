# 🚨🚨 RAWREEL DEVLOG — READ THIS FIRST, EVERY BOT 🚨🚨

> **Any Grok Bot working on RawReel: read this file before touching anything, and add your own entry when you change something.**
> Location: `/workspace/README-FIRST_RAWREEL_DEVLOG.md` on the shared computer (a copy is also on the local `support-page` branch as `DEVLOG.md`).
> Backup HQ copy: `DEVLOG.md` in the `RawReelSupport/RawReelSupport.github.io` repo (local folder `/workspace/rawreelsupport.github.io`), shown at https://rawreelsupport.github.io/ once the boss OKs the push.

---

## ⚠️ House rules (from the boss, relayed by Italian Boss / Tony)
- **Every site push needs the boss's OK.** Don't push without it.
- No spending without the boss's OK ($0 spent, $20 reserve).
- Outreach stays as **drafts** for the boss to send.
- Legal pages (Terms/Privacy) stay **offline** until the boss fills them in.
- Don't claim any feature in public until it's built and tested.
- Ads: only 5-second skippable ones.
- Always say **"RawReel"**, never the old names.
- When the boss posts in the group, only the bot for that field and Tony answer.

## 🤖 Who's on the crew
| Bot | Role | Status |
|---|---|---|
| **Italian Boss (Tony)** | Manager, second in command after the boss. Hands out jobs and checks the work. | Active |
| **Wario** | Site building and hosting | Active; built the RawReplay path |
| **Schmeelohw** | Testing and creator outreach drafts (proposed by Tony); built the Support page | Active |

## 🔑 Shared setup on this computer
- Site repo: `RawReel/rawreel.github.io`, cloned at `/workspace/rawreel.github.io`. Live at https://rawreel.github.io/
- `gh` CLI on the box is **logged in as RawReel** (scopes: repo, workflow, gist, read:org) as of 2026-10-23.
- `rawreelsupport.github.io` was first dropped (Support lives at `/support` on the main site), then **revived as the crew's backup HQ** for this devlog (boss's call, 2026-10-23). It lives in the free GitHub **organization RawReelSupport** (https://github.com/RawReelSupport), owned by the RawReel account, contact email `rawreelhq@mail.grokbot.com`. A separate account sign-up was blocked by GitHub, so we used an org instead.
- Bot email inbox: **rawreelhq@mail.grokbot.com** (Schmeelohw's). Public support email stays **RR.Support.Agent@gmail.com**.
- Support email used site-wide: **RR.Support.Agent@gmail.com**

---

## 📜 Log (newest first)

### 2026-10-23 — Schmeelohw — Backup HQ site (⛔ NOT PUSHED, boss's OK needed)
- Built the backup HQ as a static site in **`/workspace/rawreelsupport.github.io`** (branch `main`), meant for the repo `RawReelSupport/RawReelSupport.github.io`. The RawReelSupport org now exists (created 2026-10-23), but **nothing is pushed** yet.
- Pages: `index.html` (this devlog, with a READ THIS FIRST banner) and `support.html` (same content as the main site's unpushed Support page, with links pointing to https://rawreel.github.io/).
- Same look as the main site: copied `style.css`, `settings.js`, the favicons and app icons, and reused the faq.html header and footer.
- `DEVLOG.md` is the editable source. Run `python3 build.py` (needs the `markdown` package) to regenerate `index.html`.
- **Next:** push only with the boss's OK.

### 2026-10-23 — Schmeelohw — Support page (⛔ NOT PUSHED, boss said hold)
- Checked: `/support` did not exist (404 live, not in repo).
- Built `support.html` on the local branch **`support-page`** (commit `b397abd`). It is **not pushed**.
  - Contains the contact section (RR.Support.Agent@gmail.com), all 9 FAQ answers word for word, channel backup (Takeout), submitting a video, Classics, rules/removals/appeals, RawReplay (labeled as a prototype), settings/privacy, accounts, and sponsors/ads.
  - Same look as faq.html (head, header, More menu, footer, `.rule` and `details.faq` styles).
- Also changed on that branch: `nav.js` (Support added to the More menu, and the active state now works without `.html`), the same More-menu link added to 21 HTML pages, 2 lines in `style.css`, and a `sitemap.xml` entry. 25 files, +188/−1.
- Known existing bug, not touched: faq.html's built-in menu marks "About RawReel" as current (nav.js fixes it at runtime).
- Screenshots: `/workspace/support-desktop.png`, `/workspace/support-phone.png`
- **Next:** waiting for the boss's OK to push `support-page`.

### 2026-10-23 — Wario — /RawReplay/ path (⛔ NOT PUSHED, boss said hold)
- RawReplay already lives at `/replay.html` (plus `releases.html`, `artist.html`, `album.html`, `submit.html`, `replay-rules.html`, `replay.css`, `replay-*.js`).
- Added `RawReplay/index.html`, which redirects to `/replay.html` and keeps the query string and hash.
- Added a one-line script to `404.html` that sends `/rawreplay`, `/raw-replay`, and any capitalization to `/replay.html`. Tested locally; every asset loads.
- Committed locally as `118bf36` on branch **`rawreplay-directory`** in **`/workspace/rawreel-rawreplay`** (a separate folder), branched from origin/main `d7d5a29`. **Not pushed.**
- **Next:** push when the boss OKs it.
- **Gotchas:**
  1. Wario's work and Schmeelohw's `support-page` branch are in separate folders and independent. ⚠️ Both branches touch `404.html`, so expect a small merge conflict when both are merged.
  2. GitHub Pages paths are case-sensitive, but **don't add both `RawReplay/` and `rawreplay/` folders**. They clash on Mac and Windows checkouts. Use the 404.html redirect instead.
  3. RawReplay pages use root-relative links, so moving them into a subfolder would mean rewriting them.
