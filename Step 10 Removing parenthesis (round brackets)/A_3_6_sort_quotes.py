# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:05:17 2018

@author: Max
"""
#DESCRIPTION: 
# use "new_A_3_1.xml" output to to "new_A_3_6.xml"
# insert "quotes" in one "cit"  

def getkey(f):
    return f.findtext("usg", "S")

from lxml import etree

tree = etree.parse('XML/sort_test_in.xml')
entries = tree.xpath(".//entry")
n = 0
for e in entries:
    senses = tree.xpath(".//entry/sense")
    for s in senses: 
        new_cit = etree.SubElement(s, "cit", type="translation")
        quote_en = etree.SubElement(new_cit, "quote", xmllang="en")
        quote_de = etree.SubElement(new_cit, "quote", xmllang="de")
        quote_fr = etree.SubElement(new_cit, "quote", xmllang="fr")
        
tree.write("XML/sort_test_out" +"{}.xml".format(n), encoding="utf-8", pretty_print=True)

'''
        container = []
        cits = s.xpath(".//cit")
        for c in cits: 
            container.append(c)
        for x in container:
            if (x.attrib).get('{http://www.w3.org/XML/1998/namespace}lang') == "de":
                quote = x.find("quote")
                new_cit.insert(0, quote)
'''