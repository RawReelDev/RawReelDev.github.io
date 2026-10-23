# RawReel backup HQ

Backup HQ for the RawReel bot crew (every Grok Bot working on RawReel). Meant for `RawReelDev/RawReelDev.github.io` → https://rawreeldev.github.io/. Main site: https://rawreel.github.io/

## Pages
- `index.html`: the devlog, with the READ THIS FIRST banner. **Generated from `DEVLOG.md`.**
- `support.html`: a copy of the main site's Support page. Links to other RawReel pages go to https://rawreel.github.io/.

## Adding to the devlog
1. Add your entry to `DEVLOG.md` under **Log (newest first)**, at the top of the list: `### YYYY-MM-DD — Your bot name — What you did (pushed or not)`.
2. Run `python3 build.py` (needs `pip install markdown`) so `index.html` matches `DEVLOG.md`. Never edit `index.html` by hand.
3. `python3 build.py --support` re-imports `support.html` from the main repo's `support-page` branch.
4. Commit. **Don't push without the boss's OK.**

House rules: always say "RawReel", don't claim features that aren't built and tested, no Terms/Privacy pages, and the support email is RR.Support.Agent@gmail.com.

Look and feel: `style.css`, `settings.js`, the icons and `avatars/13-head-grey.png` are copied from the main site; `hq.css` and `hq.js` are the HQ's small additions.
