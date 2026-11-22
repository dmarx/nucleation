import sys, xml.etree.ElementTree as ET, re

path = sys.argv[1]
t = ET.parse(path); r = t.getroot()
art = r.find('article')

def txt(el):
    return re.sub(r'\s+', ' ', ''.join(el.itertext())).strip() if el is not None else ''

# metadata
am = art.find('.//article-meta')
title = txt(am.find('.//article-title'))
print('TITLE:', title)
print('=' * 70)
ab = art.find('.//abstract')
print('ABSTRACT:\n', txt(ab))
print('=' * 70)

def walk(sec, depth=0):
    ti = sec.find('title')
    if ti is not None:
        print('\n' + '#' * (depth + 1) + ' ' + txt(ti))
    for child in sec:
        if child.tag == 'sec':
            walk(child, depth + 1)
        elif child.tag == 'p':
            print(txt(child))
        elif child.tag in ('fig', 'table-wrap'):
            lbl = child.find('.//label'); cap = child.find('.//caption')
            print(f'[{child.tag} {txt(lbl)}] {txt(cap)}')

body = art.find('body')
for sec in body.findall('sec'):
    walk(sec)
