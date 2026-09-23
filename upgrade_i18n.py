import codecs
import re

with codecs.open('app/static/i18n.js', 'r', 'utf-8') as f:
    js = f.read()

replacement = '''
// Build bidirectional maps for auto-translation of text nodes
let autoTransMapEnToHi = new Map();
let autoTransMapHiToEn = new Map();

function initAutoTransMaps() {
  const en = I18N['en'];
  const hi = I18N['hi'];
  for (const key in en) {
    if (en[key] && hi[key]) {
      autoTransMapEnToHi.set(en[key].trim(), hi[key].trim());
      autoTransMapHiToEn.set(hi[key].trim(), en[key].trim());
    }
  }
}

function autoTranslateNode(node, targetLang) {
  const text = node.nodeValue.trim();
  if (!text) return;
  
  if (targetLang === 'hi') {
    if (autoTransMapEnToHi.has(text)) {
      node.nodeValue = node.nodeValue.replace(text, autoTransMapEnToHi.get(text));
    }
  } else if (targetLang === 'en') {
    if (autoTransMapHiToEn.has(text)) {
      node.nodeValue = node.nodeValue.replace(text, autoTransMapHiToEn.get(text));
    }
  }
}

/**
 * Apply translations to all elements with [data-i18n] attributes AND auto-translate text nodes
 */
function applyTranslations(lang) {
  if (autoTransMapEnToHi.size === 0) initAutoTransMaps();
  
  const dict = I18N[lang] || I18N['en'];
  
  // 1. Data attribute translation
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (dict[key]) {
      if (!el.hasAttribute('data-i18n-original')) {
        el.setAttribute('data-i18n-original', el.textContent);
      }
      el.textContent = dict[key];
    }
  });
  
  // 2. Placeholder translation
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.getAttribute('data-i18n-placeholder');
    if (dict[key]) {
      el.placeholder = dict[key];
    }
  });

  // 3. Auto-translate all text nodes that match dictionary strings
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
  let node;
  while ((node = walker.nextNode())) {
    // Skip script and style tags
    if (node.parentElement && (node.parentElement.tagName === 'SCRIPT' || node.parentElement.tagName === 'STYLE')) {
      continue;
    }
    autoTranslateNode(node, lang);
  }
}
'''

# Find where function applyTranslations(lang) starts
idx = js.find('function applyTranslations(lang)')
if idx != -1:
    end_idx = js.find('function switchLanguage', idx)
    js = js[:js.rfind('/**', 0, idx)] + replacement + js[end_idx:]

    with codecs.open('app/static/i18n.js', 'w', 'utf-8') as f:
        f.write(js)
    print("i18n.js upgraded to auto-translate!")
else:
    print("Could not find applyTranslations.")
