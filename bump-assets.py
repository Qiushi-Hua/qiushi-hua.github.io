"""Stamp style.css and site.js with a version so a changed file gets a new URL.

GitHub Pages serves assets with Cache-Control: max-age=600, so without this a
visitor who loaded the old stylesheet sees the new HTML against it for up to
ten minutes. Run this with a fresh number after every style.css or site.js edit.
"""
import glob, io, re, sys

ver = sys.argv[1]
pat = re.compile(r'(href="style\.css|src="site\.js)(\?v=[^"]*)?"')

for f in sorted(glob.glob('*.html')):
    s = io.open(f, encoding='utf-8').read()
    out, n = pat.subn(lambda m: '%s?v=%s"' % (m.group(1), ver), s)
    if n:
        io.open(f, 'w', encoding='utf-8', newline='\n').write(out)
    print('%-16s %d reference(s) stamped v=%s' % (f, n, ver))
