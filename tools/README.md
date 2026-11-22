# Site tools

The pages of this website are generated. Do not edit the `index.html` files by hand; change the source here and rebuild.

| File | What it is |
|---|---|
| `sitegen.py` | Writes every page, `sitemap.xml`, `robots.txt` and the 404 page into the repository root |
| `site.css` | The stylesheet. It is copied to `assets/style.css` |
| `site.js` | Theme toggle, mobile menu and the font tester. It is copied to `assets/site.js` |
| `logo/tantry-logo.svg` | The calligraphic mark shown in the home page hero |
| `check.py` | Checks every page for broken local links, invalid structured data and stray spellings |

## Rebuild

From the repository root:

```bash
python tools/sitegen.py
python tools/check.py
```

Both need only Python 3 (no packages). Then commit and push; GitHub Pages publishes the result.

When you change `site.css` or `site.js`, also bump the `?v=` number on their links in `sitegen.py` so visitors get the new file straight away.

The Tulu Transliterator is a separate repository, [`tulu-transliterator`](https://github.com/TantryTuluFonts/tulu-transliterator), published under the same address.

## Do not delete

`googlebfe5afd795b599f0.html` in the repository root is the Google Search Console ownership file. The generator does not touch it. If it is removed, Search Console stops treating the site as verified.
