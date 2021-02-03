# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 17:10:33 2018

@author: Max
"""

#!/usr/bin/python

from lxml import etree
#from copy import deepcopy
import csv
import codecs  # necessary for saving Coptic Unicode


file_name = 'CSV/CLL_Bohairic.csv'   
outfile = codecs.open(file_name, 'w', encoding='utf-8')
writer = csv.writer(outfile, delimiter=',',dialect='excel', quotechar='"')
row = ('COPT_LEMMA', 'POS 1', 'POS 2','FORMS', 'SENSES' ) 
writer.writerow(row)

#input tree
tree = etree.parse('XML_out/001.xml')


entries = tree.xpath(".//entry")
forms_non_lemma = tree.xpath(".//entry/form[not(@lemma)]")
print (len(entries), "entries")
print (len(forms_non_lemma), "forms")

for e in entries:
    
    if e.get("type")== "1":
        lemma = e.find("form[@type='lemma']/orth").text
        forms = e.xpath("./form[not(@type)]/orth/text()")
        form_elements = e.findall("form")
        for f in form_elements: 
            if f.findtext("orth", "") == "":
                print("Orth is absent in lemma: ", lemma)
        pos_1 = e.xpath("./gramGrp/pos[@type='pos_1']/text()")
        pos_2 = e.xpath("./gramGrp/pos[@type='mot']/text()")
        senses = e.xpath("./sense/cit/text()")
    #    if e.findtext("sense/cit/bibl", "") == "": 
    #          print ("Pos is absent in lemma: ", lemma)
        row = (lemma, pos_1, pos_2, forms, senses)
        writer.writerow(row)

outfile.close()
            
