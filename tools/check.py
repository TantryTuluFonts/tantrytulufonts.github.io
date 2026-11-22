import os, re, json, glob
root = '.'
bad = []; pages = 0
for f in [f for f in glob.glob(root + '/**/*.html', recursive=True) if not f.startswith('./tools')]:
    h = open(f, encoding='utf-8').read(); pages += 1
    if 'Tantri' in h: bad.append((f, 'contains Tantri'))
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    if m:
        try: json.loads(m.group(1))
        except Exception as e: bad.append((f, 'bad JSON-LD ' + str(e)))
    for href in re.findall(r'(?:href|src)="(/[^"#?]*)', h):
        t = os.path.join(root, href.lstrip('/'))
        if href.endswith('/'): t = os.path.join(t, 'index.html')
        if href.startswith('/tulu-transliterator/'): continue   # served from its own repository
        if not os.path.exists(t): bad.append((f, 'missing ' + href))
print('pages checked:', pages); print('problems:', bad if bad else 'none')
