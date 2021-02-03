# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:05:17 2018

@author: Max
"""

#DESCRIPTION: 
# "new_A_3.xml" is a copy of "new_A_2.2.xml" 
# 1) strip all spellings in <orth> 
# 2) put all spellings, which are stiil direct in <form> in <orth>, also stripping them

#import re  
from lxml import etree
#from copy import deepcopy

def xstr(s):
    if s is None:
        return ''
    return str(s.strip())

tree = etree.parse('XML/new_A_3.xml')
entries = tree.xpath(".//entry")
n = 0
for e in entries:
    forms = e.xpath(".//form")
    for f in forms:
        if f.xpath(".//orth"):
            orth = f.find(".//orth")
            orth.text = xstr(f.findtext('orth'))            
        if not f.xpath(".//orth"):
            orth = etree.SubElement(f, "orth")
            orth.text = xstr(f.text)
            f.insert(0, orth)
            n = n +1
            print (n, str((f.attrib).get('{http://www.w3.org/XML/1998/namespace}id', 'no')), str(f.text))
            f.text = None
tree.write("XML/new_A_3_1.xml", encoding="utf-8", pretty_print=True)