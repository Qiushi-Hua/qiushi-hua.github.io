"""Stamp style.css and site.js with a version so a changed file gets a new URL.

GitHub Pages serves assets with Cache-Control: max-age=600. Without this, a
visitor who already has the old stylesheet renders the new HTML against it for
up to ten minutes. Run with a fresh number after every style.css or site.js
edit, then commit:

    python bump-assets.py 8

404.html links its assets absolutely, because Pages serves that page for any
path depth and a relative link would resolve against the wrong directory.
"""
import glob, io, re, sys

ver = sys.argv[1]
pat = re.compile(
    r'((?:href|src)="(?:https://qiushi-hua\.github\.io/)?(?:style\.css|site\.js))(\?v=[^"]*)?"'
)

for f in sorted(glob.glob('*.html')):
    s = io.open(f, encoding='utf-8').read()
    out, n = pat.subn(lambda m: '%s?v=%s"' % (m.group(1), ver), s)
    if n:
        io.open(f, 'w', encoding='utf-8', newline='\n').write(out)
    print('%-16s %d reference(s) stamped v=%s' % (f, n, ver))
