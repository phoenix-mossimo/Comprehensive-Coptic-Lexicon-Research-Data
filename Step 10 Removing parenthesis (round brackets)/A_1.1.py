# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:05:17 2018

@author: Max
"""
import re  
from lxml import etree
# import csv
# import codecs  # necessary for saving Coptic Unicode
from copy import deepcopy

def xstr(s):
    if s is None:
        return ''
    return str(s.strip())

def A1_1f(s): 
    return (re.sub("\(.*\)", re.search('\((.*)\)', form_text).group(1), s)) # of (XXX) return XXXX for text in forms; ( … ) is a capturing group in regex
def A1_1o(s): 
    return (re.sub("\(.*\)", re.search('\((.*)\)', orth_text).group(1), s)) # of (XXX) return XXXX for text in orths; ( … ) is a capturing group in regex 

#file_name = 'CSV/nonlemma_nonwhitespace.csv'   
#outfile = codecs.open(file_name, 'w', encoding='utf-8')
#writer = csv.writer(outfile, delimiter=',',dialect='excel', quotechar='"')
#row = ('No', 'FORM ID', 'TYPE', 'SPELLING') 
#writer.writerow(row)


tree = etree.parse('XML/BBAW_Lexicon_of_Coptic_Egyptian-v3-2019_test.xml')
entries = tree.xpath(".//entry")
n = 0
for e in entries:
    #    forms = e.xpath(".//form[not(@type='lemma')]")
    forms = e.xpath(".//form")
    for f in forms:
        form_id = str((f.attrib).get('{http://www.w3.org/XML/1998/namespace}id', '')) #namespace is used instead of 'xml:d' 
        form_text = xstr(f.text)     
        if  re.search ('^\(.*\)$', form_text):
            n = n +1
            f1_copy = deepcopy(f)
            f1_copy.text = ("*" + A1_1f(form_text))
            if f.get('type', ' ') == 'lemma': 
                e.insert(0, f1_copy)
                e.remove(f)
            else: 
                e.insert(1, f1_copy)
                e.remove(f)
            print ("|", n, "|", form_id, "|", "form " + f.get('type', ' ') + str(f.find('./oRef'))[9:13], "|", form_text, "|", "*" + A1_1f(form_text), "|", "done",  "|", "---", "|")
#            row = (n, form_id, "form", form_text)
#            writer.writerow(row)
        orth_text = xstr(f.findtext("orth", ""))
        if  re.search ('^\(.*\)$', orth_text):
            n = n +1
            f1_copy = deepcopy(f)
            f1_copy.find('orth').text = ("*"+ A1_1o(orth_text))
            if f.get('type', ' ') == 'lemma': 
                e.insert(0, f1_copy)
                e.remove(f)
            else: 
                e.insert(1, f1_copy)
                e.remove(f)
            print ("|", n, "|", form_id, "|", "orth " + f.get('type', ' ') + str(f.find('./oRef'))[9:13], "|", orth_text, "|", "*" + A1_1o(orth_text), "|", "done",  "|", "---", "|")
#            row = (n, form_id, "orth", orth_text)
 #           writer.writerow(row)
tree.write("XML/new_A_1.1.xml", encoding="utf-8", pretty_print=True)
#outfile.close()
