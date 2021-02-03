# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:05:17 2018

@author: Max
"""
#DESCRIPTION: 
# use "new_A_3_1.xml" output to to "new_A_3_2.xml"
# soft forms according to the dialects 
# not sure if the new forms are inserted, what happens to the forms existing in the entry? removed?

def getkey(f):
    return f.findtext("usg", "S")

from lxml import etree

tree = etree.parse('XML/sort_test_in.xml')
entries = tree.xpath(".//entry")
n = 0
for e in entries:
    container = []
    forms = e.xpath(".//form[not(@type='lemma')]")
    print (str((e.attrib).get('{http://www.w3.org/XML/1998/namespace}id', 'not yet')))
    for f in forms: 
        container.append(f) 
    container = sorted(container, key=getkey, reverse=True)
    for x in container:
        print ("Before insert:", e.xpath(".//form[not(@type='lemma')]/usg/text()"))
        e.insert(0, x)
        n = n +1
        tree.write("XML/sort_test_out" +"{}.xml".format(n), encoding="utf-8", pretty_print=True)