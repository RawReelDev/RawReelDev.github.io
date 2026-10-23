#!/usr/bin/env python3
"""Build the RawReel backup HQ pages.

  python3 build.py                      # regenerate index.html from DEVLOG.md
  python3 build.py --support [REPO]     # also re-import support.html from the main site's
                                        # support-page branch (default /workspace/rawreel.github.io)

Needs the `markdown` package (pip install markdown).
"""
import html, re, subprocess, sys
import markdown

MAIN = 'https://rawreel.github.io/'
HQ = 'https://rawreeldev.github.io/'

def head(title, path, desc):
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title><link rel="stylesheet" href="style.css?v=27"><link rel="stylesheet" href="hq.css?v=1"><script src="settings.js?v=27"></script><!-- RawReel: favicon / app icons / manifest / social --><link rel="icon" href="favicon.ico" sizes="16x16 32x32 48x48"><link rel="icon" type="image/svg+xml" href="favicon.svg"><link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png"><link rel="icon" type="image/png" sizes="16x16" href="favicon-16.png"><link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon-180.png"><link rel="manifest" href="site.webmanifest"><link rel="canonical" href="{HQ}{path}"><meta property="og:url" content="{HQ}{path}"><meta name="theme-color" content="#56983A"><meta property="og:type" content="website"><meta property="og:site_name" content="RawReel"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta name="description" content="{html.escape(desc)}"><meta property="og:image" content="{HQ}og-image-1200x630.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{HQ}og-image-1200x630.png"></head>
<body>
'''

def header(page):
    def cur(p): return ' aria-current="page"' if p == page else ''
    return f'''<header>
  <a class="logo" href="index.html"><span class="orb"></span><span class="wordmark">Raw<b>Reel</b></span><small class="tagline">Backup HQ</small></a>
  <form class="search" role="search" action="{MAIN}search.html" method="get"><input type="search" name="q" placeholder="Search classics and channels" aria-label="Search classics and channels" enterkeyhint="search"><button>Search</button></form>
  <nav class="mainnav" aria-label="Main">
    <a class="ghost nav-home" href="index.html"{cur('index.html')}>Devlog</a>
    <a class="ghost" href="support.html"{cur('support.html')}>Support</a>
    <a class="ghost nav-submit" href="{MAIN}classics.html">Classics</a>
    <a class="btn" href="{MAIN}">Main site</a>
    <details class="more">
      <summary class="ghost">More</summary>
      <div class="more-menu">
        <a href="index.html"{cur('index.html')}>Devlog (READ THIS FIRST)</a>
        <a href="support.html"{cur('support.html')}>Support</a>
        <a href="mailto:RR.Support.Agent@gmail.com">Email support</a>
        <hr>
        <a href="{MAIN}">RawReel main site</a>
        <a href="{MAIN}classics.html">Classics</a>
        <a href="{MAIN}replay.html">Music</a>
        <a href="{MAIN}import.html">Back up your channel</a>
        <a href="{MAIN}upload.html">Submit a video</a>
        <a href="{MAIN}rules.html">Rules</a>
        <a href="{MAIN}replay-rules.html">Music rules</a>
        <a href="{MAIN}about.html">About RawReel</a>
        <a href="{MAIN}faq.html">FAQ</a>
        <a href="{MAIN}settings.html"><span aria-hidden="true">⚙</span> Settings</a>
        <button type="button" class="rr-theme-toggle">Theme: Light</button>
      </div>
    </details>
  </nav>
</header>
'''

FOOTER = f'''<footer class="hq-foot"><b>RawReel backup HQ</b> · the crew's devlog and a copy of the Support page · Main site: <a href="{MAIN}">{MAIN}</a> · <a href="support.html">Support</a> · <a class="footer-faq" href="{MAIN}faq.html">FAQ</a></footer>

<script src="hq.js?v=1"></script>
</body></html>
'''

BANNER = '''<div class="hq-banner" role="note" id="read-this-first">
  <h2>🚨 READ THIS FIRST 🚨</h2>
  <p><b>Every Grok Bot working on RawReel:</b> read this whole devlog before you touch anything, and add your own entry (newest first) when you change something.</p>
  <p>Edit <code>DEVLOG.md</code> in this repo, then run <code>python3 build.py</code> so this page stays in sync. <b>Nothing gets pushed without the boss's OK.</b></p>
</div>
'''

def build_index():
    md = open('DEVLOG.md', encoding='utf-8').read()
    body = markdown.markdown(md, extensions=['tables', 'sane_lists'])
    body = body.replace('<table>', '<div class="table-wrap"><table>').replace('</table>', '</table></div>')
    body = re.sub(r'(?<!href=")(https?://[^\s<]+[^\s<.,)])', r'<a href="\1">\1</a>', body)
    out = (head('RawReel backup HQ: devlog', '', 'The RawReel bot crew\'s backup HQ and devlog. Main site: https://rawreel.github.io/')
           + header('index.html') + BANNER
           + '<div class="panel doc devlog">\n' + body + '\n</div>\n' + FOOTER)
    open('index.html', 'w', encoding='utf-8').write(out)
    print('wrote index.html')

LOCAL = {'support.html'}

def build_support(repo):
    src = subprocess.check_output(['git', '-C', repo, 'show', 'support-page:support.html'], text=True)
    m = re.search(r'<div class="panel doc about support">.*?\n</div>\n(?=<footer>)', src, re.S)
    main = m.group(0)
    def fix(mo):
        h = mo.group(1)
        if re.match(r'(https?:|mailto:|#)', h) or h.split('#')[0] in LOCAL: return mo.group(0)
        return f'href="{MAIN}{h}"'
    main = re.sub(r'href="([^"]*)"', fix, main)
    out = (head('Support - RawReel', 'support.html', 'RawReel support: the full FAQ, backups, rules and appeals, music, settings, and how to reach the team.')
           + header('support.html') + main + FOOTER)
    open('support.html', 'w', encoding='utf-8').write(out)
    print('wrote support.html')

if __name__ == '__main__':
    build_index()
    if '--support' in sys.argv:
        i = sys.argv.index('--support')
        build_support(sys.argv[i + 1] if len(sys.argv) > i + 1 else '/workspace/rawreel.github.io')
