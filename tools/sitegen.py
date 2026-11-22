import json, os, html
HERE = os.path.dirname(os.path.abspath(__file__))   # the tools/ folder
ROOT = os.path.dirname(HERE)                          # the site (repository root)
BASE = 'https://tantrytulufonts.github.io'
TODAY = '2026-11-23'
GH = 'https://github.com/TantryTuluFonts'
OFL = 'https://openfontlicense.org'
TRANS = 'https://tantrytulufonts.github.io/tulu-transliterator/'
BUY = 'https://api.whatsapp.com/send/?phone=918722229750&amp;text=Hello%21+I%27m+interested+in+Tulu+Varnamruta%2C+the+Tulu+script+primer.+Please+share+the+book%27s+price+and+details+on+how+to+purchase+it'
BUY_RAW = BUY.replace('&amp;', '&')
EMAIL = 'prahladtantry89@gmail.com'
DISCUSS = 'https://github.com/orgs/TantryTuluFonts/discussions'

PERSON = {
    '@type': 'Person', '@id': BASE + '/about/#prahlad-prasad-tantry',
    'name': 'Prahlad Prasad Tantry',
    'alternateName': ['Prahlad Tantry'],
    'url': BASE + '/about/',
    'jobTitle': 'Author and type designer',
    'knowsAbout': ['Tulu language', 'Tulu-Tigalari script', 'Tulu script orthography', 'Tulu fonts', 'Type design'],
    'sameAs': ['https://github.com/PrahladTantry', GH],
}
PHOTO = os.path.exists(os.path.join(ROOT, 'assets', 'prahlad.jpg'))
if PHOTO:
    PERSON['image'] = BASE + '/assets/prahlad.jpg'
ORG = {
    '@type': 'Organization', '@id': BASE + '/#foundry',
    'name': 'Tantry Tulu Font Foundry', 'alternateName': 'Tantry Family of Tulu Fonts',
    'url': BASE + '/', 'logo': BASE + '/assets/avatar.png',
    'founder': {'@id': PERSON['@id']}, 'sameAs': [GH],
    'contactPoint': {'@type': 'ContactPoint', 'contactType': 'general enquiries', 'email': EMAIL, 'url': BASE + '/about/#contact'},
    'description': 'Free, open-source fonts and typing tools for Tulu lipi and the Tulu-Tigalari script, designed by Prahlad Prasad Tantry.',
}

NAV = [('/', 'Home'), ('/tulu-varnamruta/', 'Book'), ('/tulu-script-standard/', 'Standard'), ('/fonts/', 'Fonts'), ('/tulu-unicode-font/', 'Unicode font'), ('/tulu-keyboard/', 'Keyboard'), ('/acctantra/', 'AccTantra'), ('/tulu-transliterator/', 'Transliterator'), ('/about/', 'About')]


import re
LOGO_SVG = re.sub(r'<title>.*?</title>', '', open(os.path.join(HERE, 'logo', 'tantry-logo.svg'), encoding='utf-8').read()).replace('#000', 'currentColor').replace('<svg ', '<svg role="img" aria-label="Tantry Tulu Font Foundry calligraphic mark" ', 1)


def page(path, title, desc, h1, body, extra_ld=None, og_image='/assets/avatar.png', card='summary', hero=None):
    url = BASE + path
    ld = [{'@context': 'https://schema.org', '@graph': [ORG, PERSON, {
        '@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': title, 'description': desc,
        'isPartOf': {'@id': BASE + '/#website'}, 'about': {'@id': ORG['@id']}, 'author': {'@id': PERSON['@id']}},
        {'@type': 'WebSite', '@id': BASE + '/#website', 'url': BASE + '/', 'name': 'Tantry Tulu Font Foundry', 'publisher': {'@id': ORG['@id']}}] + (extra_ld or [])}]
    nav = ''
    for p, n in NAV:
        cur = ' aria-current="page"' if p == path else ''
        nav += '<a href="%s"%s>%s</a>' % (p, cur, n)
    out = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="author" content="Prahlad Prasad Tantry">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Tantry Tulu Font Foundry">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}{og_image}">
<meta name="twitter:card" content="{card}">
<meta name="color-scheme" content="light dark">
<script>try{{var t=localStorage.getItem('tt-theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
<link rel="stylesheet" href="/assets/style.css?v=7">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to the content</a>
<header class="top"><div class="wrap">
<a class="brand" href="/"><img src="/assets/avatar.png" width="40" height="40" alt="Tantry Tulu Font Foundry logo"><span>Tantry Tulu Font Foundry</span></a>
<div class="tools"><nav class="nav" id="nav" aria-label="Main">{nav}</nav>
<button class="icon-btn" id="themeBtn" type="button" aria-label="Switch between light and dark theme" title="Light / dark">◐</button>
<button class="icon-btn menu-btn" id="menuBtn" type="button" aria-label="Open the menu" aria-expanded="false" aria-controls="nav">☰</button></div>
</div></header>
{hero if hero else '<section class="page-head wrap"><p class="crumb"><a href="/">Home</a></p><h1>' + h1 + '</h1></section>'}
<main id="main">
{body}
</main>
<footer class="foot">
<div class="wrap">
<div><a class="brand" href="/"><img src="/assets/avatar.png" width="36" height="36" alt=""><span>Tantry Tulu Font Foundry</span></a>
<p class="blurb" style="margin-top:14px">Free, open-source fonts and typing tools for the Tuḷu script, all designed by <a href="/about/">Prahlad Prasad Tantry</a>.</p></div>
<div><h4>Explore</h4><ul><li><a href="/tulu-varnamruta/">Tuḷu Varṇāmr̥ta, the book</a></li><li><a href="/tulu-script-standard/">The standard</a></li><li><a href="/fonts/">Fonts</a></li><li><a href="/about/">About</a></li><li><a href="/about/#contact">Contact</a></li></ul></div>
<div><h4>Tools</h4><ul><li><a href="/tulu-unicode-font/">Unicode font</a></li><li><a href="/tulu-keyboard/">Tulu keyboard</a></li><li><a href="/acctantra/">AccTantra</a></li><li><a href="{TRANS}">Tulu transliterator</a></li><li><a href="{GH}">GitHub</a></li></ul></div>
</div>
<div class="legal"><div class="wrap">All fonts are free under the <a href="{OFL}">SIL Open Font License 1.1</a>. Please keep the credit to Prahlad Prasad Tantry.</div></div>
</footer>
<script src="/assets/site.js?v=1" defer></script>
</body>
</html>
'''
    d = os.path.join(ROOT, path.strip('/'))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(out)


def font_ld(name, desc, repo, fmt):
    return {'@type': 'CreativeWork', 'name': name + ' (Tulu font)', 'description': desc, 'url': f'{GH}/{repo}',
            'creator': {'@id': PERSON['@id']}, 'publisher': {'@id': ORG['@id']},
            'license': OFL, 'encodingFormat': fmt, 'inLanguage': 'tcy', 'isAccessibleForFree': True}


FONTS = [
    ('Mallige_unicode', 'Mallige Unicode', 'TTF', 'Unicode', 'Faithful to the standard as Unicode: 86 Tulu-Tigalari characters, with OpenType shaping', 'assets/mallige-unicode.png', 450),
    ('mallige', 'Mallige', 'TTF', 'ASCII', 'Faithful to the standard, with the largest set of conjuncts', 'assets/mallige.png', 510),
    ('darage', 'Darage', 'OTF', 'ASCII', 'Calligraphic, with its Glyphs source included', 'assets/darage.png', 510),
    ('mandara', 'Mandara', 'TTF', 'ASCII', 'Bold and rounded', 'assets/mandara.png', 510),
    ('allige', 'Allige', 'TTF', 'ASCII', 'The Academy edition, forked from Mallige', 'assets/allige.png', 510),
]
FONT_LD = [font_ld(n, nt + '.', r, 'font/ttf' if f == 'TTF' else 'font/otf') for r, n, f, e, nt, i, h in FONTS]


def cards():
    s = ''
    for repo, name, fmt, enc, note, img, h in FONTS:
        s += f'''<article class="card"><img src="/{img}" alt="{name} Tulu font specimen" width="1400" height="{h}">
<h3>{name}</h3><p>{note}.</p><p class="meta"><span>{fmt}</span><span>{enc}</span></p>
<p><a href="{GH}/{repo}/releases/latest">Download {name}</a> · <a href="{GH}/{repo}">Source on GitHub</a></p></article>
'''
    return s


# ---------------- Home ----------------
HOME_HERO = f'''<section class="hero"><div class="wrap">
<div>
<p class="eyebrow">Tantry Tulu Font Foundry</p>
<h1>Tulu fonts by Prahlad Prasad Tantry</h1>
<p class="lead">Free, open-source <strong>fonts</strong> and <strong>typing tools</strong> for <strong>Tulu lipi</strong> and the <strong>Tulu-Tigalari</strong> script. Every font, the typing standard and the keyboard are designed by <a href="/about/">Prahlad Prasad Tantry</a>.</p>
<div class="cta"><a class="btn" href="/fonts/">Browse the fonts</a><a class="btn alt" href="/tulu-keyboard/">Get the Tulu keyboard</a></div>
<ul class="facts"><li><b>5</b>free fonts</li><li><b>1</b>typing standard</li><li><b>1</b>Unicode keyboard</li><li><b>1</b>book</li></ul>
</div>
<div class="mark">{LOGO_SVG}</div>
</div></section>'''

page('/',
     'Tulu Fonts | Tantry Tulu Font Foundry, by Prahlad Prasad Tantry',
     'Free, open-source Tulu fonts, a Tulu Unicode font, a Tulu keyboard and a typing standard, all designed by Prahlad Prasad Tantry.',
     'Tulu fonts by Prahlad Prasad Tantry',
     f'''<section class="tester" id="tester" aria-labelledby="tt-h">
<h2 id="tt-h">Try the fonts</h2>
<p>Type AccTantra keys and watch the font draw Tulu. The example below reads <em>Om namo Narayanaya</em>.</p>
<div class="fonts-row" role="radiogroup" aria-label="Choose a font">
<button type="button" class="chip" role="radio" aria-checked="true" data-font="darage">Darage</button>
<button type="button" class="chip" role="radio" aria-checked="false" data-font="mandara">Mandara</button>
<button type="button" class="chip" role="radio" aria-checked="false" data-font="allige">Allige</button>
<button type="button" class="chip" role="radio" aria-checked="false" data-font="mallige" title="About 2 MB, loaded only when you choose it">Mallige</button>
</div>
<label for="tIn" class="note">AccTantra keys</label>
<textarea id="tIn" rows="2" spellcheck="false" autocomplete="off" autocapitalize="off">EAamAX nEma narayNay</textarea>
<div class="preview" id="tOut" aria-live="polite" lang="tcy"></div>
<p class="status" id="tStatus" aria-live="polite"></p>
<div class="links"><a id="tLink" href="{TRANS}">Convert this text in the transliterator →</a><a href="/acctantra/">How the keys work →</a></div>
</section>

<section class="book-banner" aria-label="The book">
<a href="/tulu-varnamruta/"><img src="/assets/varnamrta-cover.jpg" alt="Cover of Tuḷu Varṇāmr̥ta, A Prescriptive Primer to the Tuḷu Script, by Prahlad Prasad Tantry" width="937" height="1679"></a>
<div><p class="eyebrow">The book and the standard</p>
<h2>Tuḷu Varṇāmr̥ta</h2>
<p class="sub">A Prescriptive Primer to the Tuḷu Script</p>
<p>Everything you need to read and write the traditional Tuḷu script, in one book. It also sets out <a href="/tulu-script-standard/"><strong>the standard for writing Tuḷu</strong></a> that the language has long lacked: the traditional script kept exactly as it is, and still ready for modern Tuḷu.</p>
<div class="cta"><a class="btn wa" href="{BUY}" rel="noopener">Buy on WhatsApp</a><a class="btn alt" href="/tulu-varnamruta/">About the book</a></div></div>
</section>

<h2>The font family</h2>
<div class="grid">{cards()}</div>

<h2>Typing and tools</h2>
<div class="grid3">
<article class="card"><h3><a href="/acctantra/">AccTantra</a></h3><p>The typing standard behind the ASCII fonts. One key map, every font.</p></article>
<article class="card"><h3><a href="/tulu-keyboard/">Tulu keyboard</a></h3><p>A Keyman keyboard that types Tulu-Tigalari as real Unicode text.</p></article>
<article class="card"><h3><a href="{TRANS}">Tulu transliterator</a></h3><p>Converts between AccTantra text, IAST, Devanagari, Kannada and Malayalam.</p></article>
</div>

<h2>Common questions</h2>
<details class="q"><summary>Is there a Unicode font for Tulu?</summary><p>Yes. <a href="/tulu-unicode-font/">Mallige Unicode</a> is a free Unicode font for the Tulu-Tigalari script (Unicode 16.0), with OpenType shaping for conjuncts and marks.</p></details>
<details class="q"><summary>How do I type in Tulu?</summary><p>For real Unicode text, install the <a href="/tulu-keyboard/">AccTantra Unicode keyboard</a> for Keyman. For the ASCII fonts, type with the <a href="/acctantra/">AccTantra</a> key map on any keyboard.</p></details>
<details class="q"><summary>Are the Tulu fonts free?</summary><p>Yes. All of them are released under the SIL Open Font License 1.1: free to use, study, share and modify, as long as they are not sold on their own.</p></details>
<details class="q"><summary>Is there a standard for writing the Tulu script?</summary><p>Yes. <a href="/tulu-varnamruta/">Tuḷu Varṇāmr̥ta</a> by Prahlad Prasad Tantry sets out one rule-governed orthography for the traditional Tuḷu script, and <a href="/tulu-script-standard/">this page explains why it should be maintained</a>.</p></details>
<details class="q"><summary>Who designs these fonts?</summary><p>All of them are designed by <a href="/about/">Prahlad Prasad Tantry</a>.</p></details>''',
     FONT_LD, hero=HOME_HERO)

# ---------------- Fonts ----------------
page('/fonts/',
     'Free Tulu Fonts: Mallige Unicode, Mallige, Darage | Prahlad Prasad Tantry',
     'Download free Tulu fonts: Mallige Unicode for Tulu-Tigalari, Mallige, Darage, Mandara and Allige. Designed by Prahlad Prasad Tantry, SIL Open Font License.',
     'Free Tulu fonts',
     f'''<p class="lead">Five fonts for Tulu lipi, all designed by <a href="/about/">Prahlad Prasad Tantry</a> and free under the <a href="{OFL}">SIL Open Font License 1.1</a>. One is a <strong>Unicode</strong> font; four are <strong>ASCII</strong> fonts typed with the <a href="/acctantra/">AccTantra</a> key map.</p>
<p><strong>Mallige</strong> and <strong>Mallige Unicode</strong> are the faithful representations of <a href="/tulu-script-standard/">the standard for writing Tuḷu</a> set out in <a href="/tulu-varnamruta/">Tuḷu Varṇāmr̥ta</a>. The same work is being extended to the other fonts, and they are being ported to Unicode as well, except for Allige, which was forked from Mallige.</p>
<div class="grid">{cards()}</div>
<h2>ASCII or Unicode?</h2>
<table>
<tr><th></th><th>ASCII fonts</th><th>Unicode font</th></tr>
<tr><td>Fonts</td><td>Mallige, Darage, Mandara, Allige</td><td>Mallige Unicode</td></tr>
<tr><td>How you type</td><td>AccTantra keys on any keyboard</td><td>The AccTantra Unicode keyboard</td></tr>
<tr><td>What is stored</td><td>Latin letters, drawn as Tulu by the font</td><td>Real Tulu-Tigalari characters</td></tr>
<tr><td>Search and copy-paste</td><td>Breaks if the font is lost</td><td>Works everywhere</td></tr>
<tr><td>Best for</td><td>Print, posters, design work, legacy documents</td><td>Web, data and archives</td></tr>
</table>
<h2>Installing a font</h2>
<p><strong>Windows:</strong> right-click the font file and choose Install. <strong>macOS:</strong> open the file and click Install Font. <strong>Linux:</strong> copy it to <code>~/.local/share/fonts/</code> and run <code>fc-cache -f</code>.</p>''',
     FONT_LD)

# ---------------- Unicode font ----------------
page('/tulu-unicode-font/',
     'Tulu Unicode Font: Mallige Unicode for Tulu-Tigalari | Prahlad Prasad Tantry',
     'Mallige Unicode is a free Unicode font for the Tulu-Tigalari script (Unicode 16.0) with OpenType shaping. Designed by Prahlad Prasad Tantry.',
     'Tulu Unicode font: Mallige Unicode',
     f'''<p class="lead"><strong>Mallige Unicode</strong> is a free Unicode font for the <strong>Tulu-Tigalari script</strong> (Unicode 16.0), designed by <a href="/about/">Prahlad Prasad Tantry</a>. Text typed with it is real Unicode text: it can be searched, copied and shown in any font that supports the script.</p>
<p>Mallige Unicode is the Unicode counterpart of <a href="/fonts/">Mallige</a>, and together they are the faithful representations of <a href="/tulu-script-standard/">the standard for writing Tuḷu</a> set out in <a href="/tulu-varnamruta/">Tuḷu Varṇāmr̥ta</a>.</p>
<img class="wide" src="/assets/mallige-unicode.png" alt="Tulu-Tigalari consonants and conjuncts in the Mallige Unicode font" width="1400" height="450">
<p class="cta"><a class="btn" href="{GH}/Mallige_unicode/releases/latest">Download Mallige Unicode</a> <a class="btn alt" href="{GH}/Mallige_unicode">Source and details</a></p>
<h2>What is in the font</h2>
<table>
<tr><th>Property</th><th>Value</th></tr>
<tr><td>Current version</td><td>1.019</td></tr>
<tr><td>Glyphs</td><td>2,014</td></tr>
<tr><td>Tulu-Tigalari characters</td><td>86, covering U+11380 to U+113E2</td></tr>
<tr><td>OpenType script</td><td><code>tutg</code> (Tulu-Tigalari)</td></tr>
<tr><td>Layout features</td><td>GSUB: akhn, blwf, liga, rphf. GPOS: kern, mark, mkmk</td></tr>
<tr><td>License</td><td><a href="{OFL}">SIL Open Font License 1.1</a></td></tr>
</table>
<h2>How to type with it</h2>
<p>Install the <a href="/tulu-keyboard/">AccTantra Unicode keyboard</a> for Keyman, which produces real Tulu-Tigalari characters for this font. To convert existing text, use the <a href="{TRANS}">Tulu transliterator</a>.</p>
<p>Conjuncts and mark positions need an application with OpenType shaping support, such as one built on HarfBuzz, DirectWrite, CoreText or Uniscribe.</p>''',
     [{'@type': 'CreativeWork', 'name': 'Mallige Unicode (Tulu-Tigalari Unicode font)', 'url': GH + '/Mallige_unicode',
       'creator': {'@id': PERSON['@id']}, 'publisher': {'@id': ORG['@id']}, 'license': OFL, 'encodingFormat': 'font/ttf',
       'inLanguage': 'tcy', 'isAccessibleForFree': True, 'version': '1.019'}])

# ---------------- Keyboard ----------------
page('/tulu-keyboard/',
     'Tulu Keyboard for Keyman: AccTantra Unicode | Prahlad Prasad Tantry',
     'A free Keyman keyboard for typing Tulu-Tigalari as Unicode, following the AccTantra typing logic. Designed by Prahlad Prasad Tantry.',
     'Tulu keyboard: AccTantra Unicode',
     f'''<p class="lead">The <strong>AccTantra Unicode</strong> keyboard lets you type the <strong>Tulu-Tigalari script</strong> on a normal keyboard. It runs on <a href="https://keyman.com">Keyman</a> and was created by <a href="/about/">Prahlad Prasad Tantry</a>.</p>
<p class="cta"><a class="btn" href="{GH}/AccTantra_Unicode/releases/latest">Download the keyboard</a> <a class="btn alt" href="/tulu-unicode-font/">Get the Unicode font</a></p>
<h2>At a glance</h2>
<table>
<tr><th>Property</th><th>Value</th></tr>
<tr><td>Engine</td><td>Keyman 15.0 or later</td></tr>
<tr><td>Script</td><td>Tulu-Tigalari (Unicode U+11380 to U+113FF)</td></tr>
<tr><td>Keyboard version</td><td>1.4.2</td></tr>
<tr><td>Output</td><td>Real Unicode text, so it can be searched and copied</td></tr>
<tr><td>License</td><td><a href="{OFL}">SIL Open Font License 1.1</a></td></tr>
</table>
<h2>Using it</h2>
<p>Install the keyboard in Keyman, then install a Unicode font that supports the script, such as <a href="/tulu-unicode-font/">Mallige Unicode</a>, so the characters display. The full typing guide, with every key, is in the <a href="{GH}/AccTantra_Unicode">keyboard repository</a>.</p>
<p>Need to convert existing text? The <a href="{TRANS}">Tulu transliterator</a> converts between AccTantra text, IAST, Devanagari, Kannada and Malayalam.</p>''',
     [{'@type': 'SoftwareApplication', 'name': 'AccTantra Unicode (Tulu-Tigalari keyboard for Keyman)', 'url': GH + '/AccTantra_Unicode',
       'applicationCategory': 'UtilitiesApplication', 'operatingSystem': 'Keyman', 'softwareVersion': '1.4.2',
       'creator': {'@id': PERSON['@id']}, 'publisher': {'@id': ORG['@id']}, 'license': OFL, 'isAccessibleForFree': True}])

# ---------------- AccTantra ----------------
page('/acctantra/',
     'AccTantra: A Typing Standard for Tulu ASCII Fonts | Prahlad Prasad Tantry',
     'AccTantra is one key map for every ASCII Tulu font, so text typed once works in any font. Created by Prahlad Prasad Tantry.',
     'AccTantra: how to type Tulu with ASCII fonts',
     f'''<p class="lead"><strong>AccTantra</strong> is a typing standard for the Tulu language on ASCII-based fonts, created by <a href="/about/">Prahlad Prasad Tantry</a>. You type with an ordinary keyboard, and an AccTantra font draws the Tulu letters. Because every font follows the same key map, text written for one font works in all of them.</p>
<h2>Try it</h2>
<p>Type <code>EAamAX nEma narayNay</code> and every AccTantra font shows <em>Om namo Narayanaya</em>:</p>
<img class="wide" src="/assets/example.png" alt="The keys EAamAX nEma narayNay shown as Om namo Narayanaya in four Tulu fonts" width="940" height="420">
<h2>The key chart</h2>
<img class="wide" src="/assets/keychart.png" alt="AccTantra key chart: each key and the glyph it gives in Darage, Mandara, Allige and Mallige" width="1540" height="700" loading="lazy">
<h2>The name</h2>
<p><em>Accu</em> means to press or print, and <em>Tantra</em> means a text, theory, system or method. AccTantra means "the doctrine of printing".</p>
<h2>Where to learn more</h2>
<ul>
<li><a href="{GH}/AccTantra">AccTantra on GitHub</a>, with the full key map, conjunct reference and examples</li>
<li><a href="{TRANS}">Tulu transliterator</a>, to convert text to and from AccTantra</li>
<li><a href="/fonts/">The AccTantra fonts</a>: Darage, Mandara, Allige and Mallige</li>
</ul>''',
     [{'@type': 'CreativeWork', 'name': 'AccTantra typing standard for Tulu ASCII fonts', 'url': GH + '/AccTantra',
       'creator': {'@id': PERSON['@id']}, 'publisher': {'@id': ORG['@id']}, 'license': OFL, 'inLanguage': 'tcy', 'isAccessibleForFree': True}])

# ---------------- The book ----------------
BOOK_COVER = BASE + '/assets/varnamrta-cover.jpg'
BOOK_LD = {
    '@type': 'Book', '@id': BASE + '/tulu-varnamruta/#book',
    'name': 'Tuḷu Varṇāmr̥ta: A Prescriptive Primer to the Tuḷu Script',
    'alternateName': ['Tulu Varnamruta', 'Tulu Varnamrta', 'Tuḷu Varṇāmṛta'],
    'author': {'@id': PERSON['@id']},
    'illustrator': {'@type': 'Person', 'name': 'Aditya Ranjan Biswal'},
    'publisher': {'@type': 'Organization', 'name': 'Tuḷu Cultural Research Foundation'},
    'isbn': '9788118012306', 'bookFormat': 'https://schema.org/Paperback',
    'bookEdition': 'First Edition', 'datePublished': '2026', 'inLanguage': 'en',
    'genre': 'Writing systems and orthography',
    'about': ['Tulu script', 'Tulu orthography', 'Tulu-Tigalari script'],
    'image': BOOK_COVER, 'url': BASE + '/tulu-varnamruta/',
    'description': 'A primer that teaches the whole traditional Tuḷu script and proposes a standard orthography for writing Tuḷu.',
    'potentialAction': {'@type': 'OrderAction', 'target': BUY_RAW},
}

page('/tulu-varnamruta/',
     'Tulu Varnamruta: A Primer and Standard for the Tulu Script | Prahlad Prasad Tantry',
     'Tuḷu Varṇāmr̥ta teaches the whole traditional Tulu script and sets out the standard for writing Tulu. By Prahlad Prasad Tantry. Order on WhatsApp.',
     'Tuḷu Varṇāmr̥ta',
     f'''<p class="sub-title">A Prescriptive Primer to the Tuḷu Script, by <a href="/about/">Prahlad Prasad Tantry</a></p>
<div class="book-hero">
<img src="/assets/varnamrta-cover.jpg" alt="Cover of Tuḷu Varṇāmr̥ta, A Prescriptive Primer to the Tuḷu Script" width="937" height="1679">
<div>
<p class="lead">Everything you need to read and write the traditional Tuḷu script, in one book.</p>
<p>Tuḷu Varṇāmr̥ta teaches the whole script, from vowels and consonants to conjuncts and Vedic symbols, with romanization beside every example. You do not need to piece it together from multiple sources, and you do not need to know any other Indic script. By the final chapter, you are reading a complete story in Tuḷu.</p>
<p>It also introduces <a href="/tulu-script-standard/"><strong>a standard for writing Tuḷu</strong></a>, something the language has long lacked. The standard keeps the traditional script exactly as it is and still accommodates what modern Tuḷu needs.</p>
<p class="meta"><span>ISBN 978-81-180123-0-6</span><span>Paperback</span><span>First edition, 2026</span><span>B5 format</span><span>Punname Publications, an imprint of TCRF</span></p>
<p class="cta"><a class="btn wa" href="{BUY}" rel="noopener">Buy on WhatsApp</a> <a class="btn alt" href="/tulu-script-standard/">Why this standard matters</a></p>
<p class="note">Tap the button to message us on WhatsApp. The price and how to purchase are shared there.</p>
</div></div>

<h2>A standard Tuḷu has long lacked</h2>
<p>Despite its rich literary tradition and its large number of speakers, Tuḷu has never had a standardized orthography for its traditional script. Manuscripts, inscriptions and printed texts each follow their own conventions, shaped by region, by individual scribal habit, or by whatever source a writer happened to learn from. No two sources could be trusted to agree with each other.</p>
<p>Tuḷu Varṇāmr̥ta is offered as both a teaching tool and a proposed standard: one coherent, rule-governed system for writing Tuḷu, argued for on principled grounds and applied without exception. <a href="/tulu-script-standard/">Read why it should be maintained.</a></p>

<h2>What you will learn</h2>
<ul>
<li><strong>The whole script.</strong> Vowels and vowel signs, consonant letters, and the complete varṇamālā in śikṣā order.</li>
<li><strong>The logic of the letters.</strong> A classification of letters by the geometry of their terminal stroke (śirovarṇa and pucchavarṇa) that explains how signs, conjuncts and virāmas behave, so you learn rules instead of memorizing exceptions.</li>
<li><strong>Conjuncts.</strong> A catalogue of saṃyuktākṣaras, built on that same logic.</li>
<li><strong>Orthographic rules.</strong> The virāma, the repha, gemination, numerals and punctuation.</li>
<li><strong>Modern Tuḷu.</strong> A chapter on loanword orthography, from Sanskrit through to English and other modern European languages.</li>
<li><strong>Vedic marks.</strong> How the traditional script represents recited Sanskrit with its pitch accents.</li>
<li><strong>Reading.</strong> <em>Kaḍēto Pāṭha</em>, a complete Tuḷu story, to test everything you have learned.</li>
</ul>

<h2>Inside the book</h2>
<table class="parts">
<tr><th>Front matter</th><td>Maṅgalācaraṇam (invocation), dedication, the Foreword (Āśīrvacana) by Śrī Śrī Vidyēśatīrtha Svāmiḷ of Śrī Bhaṇḍārakēri Maṭha, Bārkūru, preface and acknowledgements</td></tr>
<tr><th>Part I<br><span>Linguistic and orthographic foundations</span></th><td>Scope and purpose of the primer · Conventions used in the book · The Tuḷu language and its written tradition · Phonological structure relevant to orthography</td></tr>
<tr><th>Part II<br><span>The Tuḷu script system</span></th><td>Vowels and vowel signs · Consonant letters · The Tuḷu varṇamālā · Letter geometry: śirovarṇas, pucchavarṇas and the logic of saṃyuktākṣaras · Saṃyuktākṣara catalogue · Orthographic rules and modifiers · Loanword orthography · Vedic cantillation marks</td></tr>
<tr><th>Part III<br><span>Reading</span></th><td><em>Kaḍēto Pāṭha</em>, a story in Tuḷu, a translation of Alphonse Daudet's <em>La Dernière Classe</em> (<em>The Last Lesson</em>)</td></tr>
<tr><th>Back matter</th><td>Bibliography · Glossary (terms introduced by the book are marked)</td></tr>
</table>

<h2>A blessing for the traditional script</h2>
<blockquote>
<p>What I especially admire about this work is its commitment to preserving the original form of the traditional Tuḷu script without any compromise. Our Śrī Maṭha does not support any simplification, change or unnecessary revision of the traditional Tuḷu script. It is our firm position that the script that has come to us through tradition should be preserved in its original form, taught to coming generations, and promoted. Following this very principle, the book's effort to standardize the use of the traditional Tuḷu script while retaining its original form is commendable. I wholeheartedly welcome this good work.</p>
<footer>Śrī Śrī Vidyēśatīrtha Svāmiḷ, Pīṭhādhipati, Śrī Bhaṇḍārakēri Maṭha, Bārkūru. From the Foreword to Tuḷu Varṇāmr̥ta, translated from the Kannada.</footer>
</blockquote>

<h2>Who it is for</h2>
<div class="grid3">
<article class="card"><h3>Heritage learners</h3><p>Many people grew up speaking Tuḷu but never learned to read it. The book assumes nothing and builds the script from first principles.</p></article>
<article class="card"><h3>Linguists and researchers</h3><p>Reliable script literacy is the first step to reading primary Tuḷu sources, and the book gives it.</p></article>
<article class="card"><h3>Indologists</h3><p>Get to script literacy for historical documents and regional records without learning the full language.</p></article>
<article class="card"><h3>Typographers and font makers</h3><p>Detail on letter structure, conjunct formation and orthographic reasoning for anyone building digital fonts for the script.</p></article>
</div>

<h2>From the author</h2>
<blockquote class="author">
<p>Today, I'm a software engineer who has been learning the Tuḷu script since the eighth grade. Growing up outside Tuḷunāḍụ kindled my curiosity about the script and its history, and I began piecing together what I could from documents, books, manuscripts, fonts, and whatever other sources I could find. Along the way, I began making fonts and other tools to make the script easier to use. This book is my attempt to put together the kind of book I wished I had when I first began learning the script.</p>
<footer>Prahlad Prasad Tantry, from the back cover</footer>
</blockquote>
<p>The script examples in the book are set in <a href="/fonts/">Mallige</a>, a free font published here and a faithful representation of the standard the book sets out. <a href="/tulu-unicode-font/">Mallige Unicode</a> carries the same standard into Unicode.</p>

<h2>Credits</h2>
<p>All artwork in the book, including the cover and the Maṅgalācaraṇam, was hand-drawn by <strong>Aditya Ranjan Biswal</strong>. The Foreword is by Śrī Śrī Vidyēśatīrtha Svāmiḷ of Śrī Bhaṇḍārakēri Maṭha, Bārkūru. The book was published with the support of the Tuḷu Cultural Research Foundation.</p>

<h2>How to buy</h2>
<p class="cta"><a class="btn wa" href="{BUY}" rel="noopener">Buy on WhatsApp</a></p>
<p>The button opens WhatsApp with a message already written. Send it, and the price and the details on how to purchase are shared with you there.</p>

<h2>Questions</h2>
<h3>Do I need to know another Indic script?</h3>
<p>No. The book assumes only literacy in English and basic linguistic terms, and builds the Tuḷu script from the beginning. Knowing Kannada, Malayalam or Devanagari may speed things up, but it is never required.</p>
<h3>Is it a Tuḷu language course?</h3>
<p>No. It is a script primer. It does not teach spoken Tuḷu or its grammar. It teaches you to read any Tuḷu word written in the traditional script and pronounce it correctly.</p>
<h3>Does it cover modern words?</h3>
<p>Yes. The loanword chapter sets out how each layer of borrowing is written, from the oldest Sanskrit words to English and other modern European languages.</p>
<h3>Can I quote it or copy it?</h3>
<p>You may cite, quote and reference the book in academic, scholarly, educational and other non-commercial contexts, with credit to the author. Reproducing or distributing the book, in whole or in substantial part, or publishing a reprint, translation or derivative edition, needs the written permission of the copyright holder.</p>
<h3>How should I cite it?</h3>
<p>Tantry, Prahlad Prasad. <em>Tuḷu Varṇāmr̥ta: A Prescriptive Primer to the Tuḷu Script</em>. First edition. Tuḷu Cultural Research Foundation (Punname Publications), 2026. ISBN 978-81-180123-0-6.</p>''',
     [BOOK_LD], og_image='/assets/varnamrta-card.jpg', card='summary_large_image')

# ---------------- The standard ----------------
page('/tulu-script-standard/',
     'A Standard for the Tulu Script: Why One Orthography Matters | Tuḷu Varṇāmr̥ta',
     'The traditional Tulu script has never had a standard orthography. Tuḷu Varṇāmr̥ta proposes one: the script kept exactly as it is, ready for modern Tulu.',
     'A standard for the Tulu script',
     f'''<p class="lead">Tuḷu has a long written tradition and well over a million speakers, yet its traditional script has never had a standard orthography. <a href="/tulu-varnamruta/">Tuḷu Varṇāmr̥ta</a> proposes one. <strong>We hold that it should be adopted and maintained.</strong></p>
<p class="cta"><a class="btn wa" href="{BUY}" rel="noopener">Get the book on WhatsApp</a> <a class="btn alt" href="/tulu-varnamruta/">About the book</a></p>

<h2>The problem</h2>
<p>Tuḷu script usage varies across texts, regions and periods. A learner who meets three different ways of writing the same sound has no way to proceed unless someone says which one to use. Existing resources either assume you already know a related script, lack any real prescriptive clarity, or wander into language learning that goes well beyond the script. None of them fix the inconsistency at its root.</p>
<p>The same gap affects everyone who works with the script today. Digital fonts, Unicode support and teaching materials all involve orthographic decisions, whether or not anyone admits it. Without a written standard, those decisions are made quietly, differently, and often without reasons.</p>

<h2>What the standard is</h2>
<p>Tuḷu Varṇāmr̥ta sets out one coherent, rule-governed orthography for the traditional Tuḷu script and applies it without exception. It is built on three commitments:</p>
<ol class="steps">
<li><strong>The traditional script, exactly as it is.</strong> No simplification, no invented forms, no unnecessary revision. Where existing practice was already systematic, the standard adopts it as it is.</li>
<li><strong>One rule, one answer.</strong> Where practice diverged or fell silent, the standard proposes a resolution and explains the reasoning, instead of leaving the learner with a menu of alternatives.</li>
<li><strong>Room for modern Tuḷu.</strong> The standard accommodates what the language needs today, including words borrowed from English and other modern languages.</li>
</ol>

<h2>How it works</h2>
<p>The standard rests on reasons that can be checked. A few examples:</p>
<ul>
<li><strong>Letters are classified by shape.</strong> Each consonant letter is either a <em>śirovarṇa</em> (head-letter) or a <em>pucchavarṇa</em> (tail-letter), according to where its terminal stroke ends and in what direction. That single classification explains how the u and ū signs attach, how conjuncts form, how signs behave on conjuncts, and which virāma a letter takes.</li>
<li><strong>The virāma follows the geometry.</strong> A pucchavarṇa takes the sūryavirāma and a śirovarṇa takes the chandravirāma, so there is a rule where there used to be habit.</li>
<li><strong>The gemination mark has one job.</strong> It is reserved for onomatopoeic and expressive reduplications. Every other doubled consonant uses the standard conjunct.</li>
<li><strong>Loanwords are handled layer by layer.</strong> Each sound has a defined way of being written, from Sanskrit borrowings through to English, so a modern word is not a special case.</li>
<li><strong>Every letter is paired with IAST.</strong> The romanization pins down exactly which sound and which orthographic decision each script form stands for, which makes the standard something you can check, not just trust.</li>
</ul>

<h2>Why it should be maintained</h2>
<p>A standard only works if it is kept. When books, fonts, keyboards, software and classrooms all follow the same rules, their work can be read, checked and combined. Departures from the standard become visible as departures, not as proof that no standard exists.</p>
<p>The standard also protects the script itself. The Foreword to the book puts the position plainly: the traditional Tuḷu script should be preserved in its original form, taught to coming generations, and promoted, without simplification or change. A shared standard is how that is done in practice, so that "the traditional script" means the same thing to every writer.</p>
<blockquote>
<p>It is our firm position that the script that has come to us through tradition should be preserved in its original form, taught to coming generations, and promoted.</p>
<footer>Śrī Śrī Vidyēśatīrtha Svāmiḷ, Pīṭhādhipati, Śrī Bhaṇḍārakēri Maṭha, Bārkūru, in the Foreword to Tuḷu Varṇāmr̥ta (translated from the Kannada)</footer>
</blockquote>

<h2>The reference fonts</h2>
<p>A standard needs fonts that follow it faithfully. <a href="/fonts/"><strong>Mallige</strong></a> (ASCII) and <a href="/tulu-unicode-font/"><strong>Mallige Unicode</strong></a> are the faithful representations of this standard, and the script examples in the book are set in Mallige. The same work is being extended to the other fonts in the family, and they are being ported to Unicode too, except for Allige, which was forked from Mallige.</p>

<h2>Open to argument</h2>
<p>The standard is meant to be examined, argued with and improved, not taken on faith. Every decision in the book is explained, so a reader who disagrees can see exactly where, and why. That is how a standard stays alive: by being used, tested and kept consistent.</p>

<h2>Who should adopt it</h2>
<ul>
<li><strong>Teachers and learners</strong> of the script, who need one set of rules to teach and to learn.</li>
<li><strong>Writers and publishers</strong> setting Tuḷu in the traditional script.</li>
<li><strong>Font designers and software developers</strong> deciding how the script should behave on screen. The script examples in the book are set in <a href="/fonts/">Mallige</a> and typed with the <a href="/acctantra/">AccTantra</a> key map, both published here and free to use.</li>
<li><strong>Researchers</strong> who need a stable reference for reading and citing Tuḷu material.</li>
</ul>

<h2>Read the standard</h2>
<p>The full standard, with every rule, its reasoning and its examples, is in <a href="/tulu-varnamruta/"><strong>Tuḷu Varṇāmr̥ta: A Prescriptive Primer to the Tuḷu Script</strong></a> by <a href="/about/">Prahlad Prasad Tantry</a>.</p>
<p class="cta"><a class="btn wa" href="{BUY}" rel="noopener">Buy on WhatsApp</a> <a class="btn alt" href="/tulu-varnamruta/">About the book</a></p>''',
     [BOOK_LD], og_image='/assets/varnamrta-card.jpg', card='summary_large_image')

# ---------------- About ----------------
if PHOTO:
    photo_html = '<figure class="portrait"><img src="/assets/prahlad.jpg" alt="Prahlad Prasad Tantry, Tulu type designer" width="320" height="320"><figcaption>Prahlad Prasad Tantry</figcaption></figure>'
else:
    photo_html = ''

page('/about/',
     'About Prahlad Prasad Tantry: Tulu Font Designer | Tantry Tulu Font Foundry',
     'Prahlad Prasad Tantry is the author of Tuḷu Varṇāmr̥ta and the designer of free Tulu fonts, the AccTantra typing standard and a Tulu-Tigalari Unicode font and keyboard.',
     'Prahlad Prasad Tantry',
     f'''<div class="about-head">{photo_html}<div><p class="lead"><strong>Prahlad Prasad Tantry</strong> is an author and type designer who works on the <strong>Tulu language</strong> and its script. He wrote <a href="/tulu-varnamruta/"><em>Tuḷu Varṇāmr̥ta</em></a>, a primer that teaches the traditional Tuḷu script and proposes <a href="/tulu-script-standard/">a standard for writing Tuḷu</a>, and he designed every font published by the Tantry Tulu Font Foundry, along with the typing standard and the keyboard that go with them.</p>
<p>His aim is simple: keep the traditional script exactly as it is, and make it easy to read, write and type in a modern world, with tools that anyone can use.</p></div></div>
<blockquote class="author">
<p>I have been learning the Tuḷu script since the eighth grade. Growing up outside Tuḷunāḍụ kindled my curiosity about the script and its history, and I began piecing together what I could from documents, books, manuscripts, fonts, and whatever other sources I could find. Along the way, I began making fonts and other tools to make the script easier to use.</p>
<footer>Prahlad Prasad Tantry, from the back cover of Tuḷu Varṇāmr̥ta</footer>
</blockquote>
<h2>What he has made</h2>
<div class="grid3">
<article class="card"><h3><a href="/tulu-varnamruta/">Tuḷu Varṇāmr̥ta</a></h3><p>The book: the whole traditional script, and a standard for writing Tuḷu.</p></article>
<article class="card"><h3><a href="/fonts/">Five Tulu fonts</a></h3><p>Mallige Unicode, Mallige, Darage, Mandara and Allige.</p></article>
<article class="card"><h3><a href="/acctantra/">AccTantra</a></h3><p>The typing standard that makes every ASCII Tulu font interchangeable.</p></article>
<article class="card"><h3><a href="/tulu-keyboard/">A Tulu keyboard</a></h3><p>A Keyman keyboard for typing Tulu-Tigalari as Unicode.</p></article>
</div>
<h2>Authorship</h2>
<p>Prahlad Prasad Tantry is the designer and copyright holder of all of these fonts. Every repository lists him as the author, and every font is free to use under the <a href="{OFL}">SIL Open Font License 1.1</a>. If you use them, please keep that credit.</p>
<h2 id="contact">Contact</h2>
<p>The best way to reach Prahlad depends on what you need.</p>
<div class="grid3">
<article class="card"><h3>Email</h3><p>Questions, permissions, press and collaboration.</p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></article>
<article class="card"><h3>A problem with a font</h3><p>A wrong glyph, a missing conjunct or a rendering bug. Please include the keys you typed.</p><p><a href="{GH}/.github/issues/new/choose">Report it on GitHub</a></p></article>
<article class="card"><h3>Ideas and questions</h3><p>Ask about the fonts and tools, or say what you would like built next.</p><p><a href="{DISCUSS}">Join the discussion</a></p></article>
<article class="card"><h3>Buying the book</h3><p>Message on WhatsApp for the price and how to purchase.</p><p><a href="{BUY}" rel="noopener">Message on WhatsApp</a></p></article>
</div>

<h2>Find his work</h2>
<ul>
<li><a href="{GH}">Tantry Tulu Font Foundry on GitHub</a>, where the fonts and source are published</li>
<li><a href="https://github.com/PrahladTantry">Prahlad Tantry on GitHub</a></li>
<li><a href="/fonts/">Download the fonts</a></li>
</ul>''',
     [])

# ---- sitemap, robots, 404 ----
paths = [p for p, _ in NAV]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'  <url><loc>{BASE}{p}</loc><lastmod>{TODAY}</lastmod></url>\n' for p in paths) + '</urlset>\n'
open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm)
open(os.path.join(ROOT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {BASE}/sitemap.xml\n')
open(os.path.join(ROOT, '404.html'), 'w', encoding='utf-8').write('<!doctype html><meta charset="utf-8"><title>Page not found | Tantry Tulu Font Foundry</title><meta name="robots" content="noindex"><link rel="stylesheet" href="/assets/style.css?v=6"><main class="wrap"><h1>Page not found</h1><p><a href="/">Back to the Tulu fonts</a></p></main>')
open(os.path.join(ROOT, '.nojekyll'), 'w').write('')

css = open(os.path.join(HERE, 'site.css'), encoding='utf-8').read()
open(os.path.join(ROOT, 'assets', 'site.js'), 'w', encoding='utf-8').write(open(os.path.join(HERE, 'site.js'), encoding='utf-8').read())
open(os.path.join(ROOT, 'assets', 'style.css'), 'w', encoding='utf-8').write(css)
print('pages:', paths, '| photo:', PHOTO)
