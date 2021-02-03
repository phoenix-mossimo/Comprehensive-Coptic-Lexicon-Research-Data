# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:05:17 2018

@author: Max
"""
# 1) Incert temporary IDs 
from lxml import etree

def xstr(s):
    if s is None:
        return ''
    return str(s.strip())

tree = etree.parse('XML/new_A_3_2.xml')
entries = tree.xpath(".//entry")
entry_number = 0
form_number = 0
for e in entries:    
    if str((e.attrib).get('{http://www.w3.org/XML/1998/namespace}id', 'no')) == "no": 
        entry_number = entry_number +1
        xml_id = 'C_TMP' + str(entry_number)
        e.set('{http://www.w3.org/XML/1998/namespace}id', xml_id) 
    forms = e.xpath(".//form")
    for f in forms:
        if str((f.attrib).get('{http://www.w3.org/XML/1998/namespace}id', 'no')) == "no":
            form_number = form_number +1
            xml_id = 'CF_TMP' + str(form_number)
            f.set('{http://www.w3.org/XML/1998/namespace}id', xml_id) 
tree.write("XML/new_A_3_TMP_ID.xml", encoding="utf-8", pretty_print=True)