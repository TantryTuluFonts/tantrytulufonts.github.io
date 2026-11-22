/* Tantry Tulu Font Foundry: small progressive enhancements. The site works without this file. */
(function () {
  'use strict';

  // ---- theme toggle (the initial theme is set by a tiny inline script in <head>) ----
  var root = document.documentElement;
  var themeBtn = document.getElementById('themeBtn');
  if (themeBtn) themeBtn.addEventListener('click', function () {
    var cur = root.getAttribute('data-theme') || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    var next = cur === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('tt-theme', next); } catch (e) {}
  });

  // ---- mobile menu ----
  var menuBtn = document.getElementById('menuBtn'), nav = document.getElementById('nav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', function (e) { if (e.target.tagName === 'A') { nav.classList.remove('open'); menuBtn.setAttribute('aria-expanded', 'false'); } });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { nav.classList.remove('open'); menuBtn.setAttribute('aria-expanded', 'false'); } });
  }

  // ---- live type tester (home page) ----
  var tester = document.getElementById('tester');
  if (!tester) return;
  var input = document.getElementById('tIn'), preview = document.getElementById('tOut'), status = document.getElementById('tStatus');
  var link = document.getElementById('tLink'), chips = Array.prototype.slice.call(tester.querySelectorAll('[data-font]'));
  var FONTS = {
    darage:  { family: 'TT Darage',  url: '/assets/fonts/darage.otf',  size: '84 KB' },
    mandara: { family: 'TT Mandara', url: '/assets/fonts/mandara.ttf', size: '96 KB' },
    allige:  { family: 'TT Allige',  url: '/assets/fonts/allige.ttf',  size: '93 KB' },
    mallige: { family: 'TT Mallige', url: '/assets/fonts/mallige.ttf', size: '2 MB' }
  };
  var loaded = {}, current = 'mallige', token = 0;

  function render() {
    preview.textContent = input.value;
    link.href = 'https://tantrytulufonts.github.io/tulu-transliterator/#d=tulu-iast&q=' + encodeURIComponent(input.value);
  }
  function use(key) {
    var f = FONTS[key]; current = key; var my = ++token;
    chips.forEach(function (c) { c.setAttribute('aria-checked', String(c.dataset.font === key)); });
    function apply() { if (my !== token) return; preview.style.fontFamily = "'" + f.family + "', system-ui, sans-serif"; status.textContent = ''; }
    if (loaded[key]) return apply();
    status.textContent = 'Loading ' + key.charAt(0).toUpperCase() + key.slice(1) + ' (' + f.size + ')…';
    new FontFace(f.family, 'url(' + f.url + ')').load().then(function (face) {
      document.fonts.add(face); loaded[key] = true; apply();
    }).catch(function () { if (my === token) status.textContent = 'Could not load the font. You can still download it from the fonts page.'; });
  }
  chips.forEach(function (c) { c.addEventListener('click', function () { use(c.dataset.font); }); });
  input.addEventListener('input', render);
  render();
  // start with the lightest font so the first paint is instant, then offer the others
  use('darage');
})();
