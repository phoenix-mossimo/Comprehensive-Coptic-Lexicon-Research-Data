# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:05:17 2018

@author: Max
"""
import re  
from lxml import etree

def xstr(s):
    if s is None:
        return ''
    return str(s.strip())

tree = etree.parse('XML/new_A_2.2.xml')
entries = tree.xpath(".//entry")
n = 0    
for e in entries:
    forms = e.xpath(".//form[not(@status='deprecated')]")
    for f in forms:
        form_id = str((f.attrib).get('{http://www.w3.org/XML/1998/namespace}id', 'not yet'))
        form_text = xstr(f.text)
        orth_text = xstr(f.findtext("orth", ""))
        if  re.search ('.*\(.*', form_text):
            n = n + 1
            print ("|", n, "|", form_id, "|", "form", "|", form_text, "|")
        if re.search ('.*\(.*', orth_text):
            n = n + 1
            print ("|", n, "|", form_id,"|", "orth", "|", orth_text, "|") 

