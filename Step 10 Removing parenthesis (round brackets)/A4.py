# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:32:12 2020

@author: Max
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:05:17 2018

@author: Max
"""
#DESCRIPTION: 
# going up--> down from senses, trying to find what are other properties o this group
# Elements carry attributes as a dict, so we can address the keys and values of the dictionary

from lxml import etree

tree = etree.parse('XML/new_A_3_1.xml')
entries = tree.xpath(".//entry")
for e in entries: 
#    cits = e.xpath(".//sense/cit[@type!='translation']")
    senses = e.xpath(".//sense")    
    for s in senses: 
        for x in s.values(): 
            if x=="4":
                print ((e.attrib).get('{http://www.w3.org/XML/1998/namespace}id', 'none'))
#    for c in cits :
#        if len(c.findall("./quote")) >1:
 #          print (c.findall("./quote"))
#          print (n+1) 
#           print ((e.attrib).get('{http://www.w3.org/XML/1998/namespace}id', 'none'))