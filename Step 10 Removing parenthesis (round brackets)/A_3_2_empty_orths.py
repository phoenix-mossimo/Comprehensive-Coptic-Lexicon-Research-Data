# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:05:17 2018

@author: Max
"""

#DESCRIPTION: 
#1) check if there are still forms in <form> tag
#2) print forms in <orth> containing white spaces in the beginning or in the end (#85)
#3) print <orth>s which are empty (#109)
import re  
from lxml import etree

def xstr(s):
    if s is None:
        return ''
    return str(s.strip())

tree = etree.parse('XML/new_A_3_1.xml')
entries = tree.xpath(".//entry")
x = 0
y = 0
for e in entries:    

#    if str((e.attrib).get('{http://www.w3.org/XML/1998/namespace}id', 'no')) == "no": 
#        x = x +1
#        print (x, "lemma", e.xpath("./form[(@type='lemma')]/orth/text()")) 
    forms = e.xpath(".//form")
    for f in forms:
        if len(xstr(f.text)) >1:
            print (str((f.attrib).get('{http://www.w3.org/XML/1998/namespace}id', 'no')), len(f.text))
        if re.search('^\s.', str(f.findtext("orth", ""))):
            print ("|", str((f.attrib).get('{http://www.w3.org/XML/1998/namespace}id', 'no')),"|", "orth","|", str(f.findtext("orth", "")), "|", "...|")
        if re.search('.*\s$', str(f.findtext("orth", ""))):
            print ("|", str((f.attrib).get('{http://www.w3.org/XML/1998/namespace}id', 'no')),"|", "orth","|", str(f.findtext("orth", "")), "|", "...|")
        if re.search(',', str(f.findtext("orth", ""))):
            print ("|", str((f.attrib).get('{http://www.w3.org/XML/1998/namespace}id', 'no')),"|", "orth","|", str(f.findtext("orth", "")), "|", "...|")

#        if re.search('^\s.*', str(f.text)):            
#            print ("|", str((f.attrib).get('{http://www.w3.org/XML/1998/namespace}id', 'no')), "|", "form", "|", str(f.text), "|", "...|")
        
#        str((f.attrib).get('{http://www.w3.org/XML/1998/namespace}id', 'no')) == "no":
#            y = y+1
#            print (y, "non-lemma", xstr(f.text), xstr(f.findtext("orth", "")))