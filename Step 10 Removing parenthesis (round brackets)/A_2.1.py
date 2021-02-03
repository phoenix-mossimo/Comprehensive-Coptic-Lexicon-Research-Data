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
from itertools import zip_longest


def xstr(s):
    if s is None:
        return ''
    return str(s.strip())

def A1_1f(s): 
    return (re.sub("\(.*\)", re.search('\((.*)\)', form_text).group(1), s)) # of xx(y)xx return xxYxx for text in form;
def A1_1f_(s): 
    return (re.sub("\(.*\)", '', s))                                        # of xx(y)xx return xxxx for text in form;
def A1_1o(s): 
    return (re.sub("\(.*\)", re.search('\((.*)\)', orth_text).group(1), s)) # of xx(y)xx return xxYxx for text in orth;
def A1_1o_(s): 
    return (re.sub("\(.*\)", '', s))                                        # of xx(y)xx return xxxx for text in orth;



# file_name = 'CSV/nonlemma_nonwhitespace.csv'   
# outfile = codecs.open(file_name, 'w', encoding='utf-8')
# writer = csv.writer(outfile, delimiter=',',dialect='excel', quotechar='"')
# row = ('No', 'FORM ID', 'TYPE', 'SPELLING') 
# writer.writerow(row)



tree = etree.parse('XML/new_A_1.2_new.xml')
entries = tree.xpath(".//entry")
n = 0
for e in entries:
#    forms = e.xpath(".//form[not(@type='lemma')]")
    forms = e.xpath(".//form")
    for f in forms:
        form_id = str((f.attrib).get('{http://www.w3.org/XML/1998/namespace}id', ' '))
        form_text = xstr(f.text)
        if  re.search ('\S+\(.*\)', form_text):
            n = n +1
            f1_copy = deepcopy(f)
            f2_copy = deepcopy(f)
            f1_copy.text = A1_1f(form_text)
            f2_copy.text = A1_1f_(form_text)
            if f.get('type', ' ') == 'lemma': 
                e.insert(0, f2_copy)
                e.remove(f)
                print ("|", n, "|", form_id, "|", f.findtext('usg', 'S') + " form " + f.get('type', ' ')  + str(f.find('./oRef'))[9:13], "|", form_text, "|", A1_1f_(form_text), "|", "done",  "|", "---", "|")
            else: 
                e.insert(1, f1_copy)
                e.insert(2, f2_copy)
#                etree.SubElement(f, "lbl", type="time").text = "obsolete"
#                etree.SubElement(f, "prt", type="substitutedBy", target="#CF_newform1 #CF_newform2")
                f.set('status', 'deprecated') # setting attributes of the old form                  
                f.set('corresp', 'CF_newform1 CF_newform2') # setting attributes of the old form
#                f1_copy.append(etree.Element("ptr", target=form_id))                
                f1_copy.set('status', 'added')
                f1_copy.set('corresp', form_id)
                f1_copy.attrib.pop('{http://www.w3.org/XML/1998/namespace}id')
#                f2_copy.append(etree.Element("ptr", target=form_id)) 
                f2_copy.set('status', 'added')
                f2_copy.set('corresp', form_id)
                f2_copy.attrib.pop('{http://www.w3.org/XML/1998/namespace}id')
                print ("|", n, "|", form_id, "|", f.findtext('usg', 'S') + " form " + f.get('type', ' ')  + str(f.find('./oRef'))[9:13], "|", form_text, "|", A1_1f(form_text),",", A1_1f_(form_text), "|", "done",  "|", "---", "|")
#            row = (n, form_id, "form", form_text)
#            writer.writerow(row)
        orth_text = xstr(f.findtext("orth", ""))
        if  re.search ('\S+\(.*\)', orth_text):
            n = n +1
            f1_copy = deepcopy(f)
            f2_copy = deepcopy(f)
            f1_copy.find('orth').text = A1_1o(orth_text)
            f2_copy.find('orth').text = A1_1o_(orth_text)
            if f.get('type', ' ') == 'lemma': 
                e.insert(0, f2_copy)
                e.remove(f)
                print ("|", n, "|", form_id, "|", f.findtext('usg', 'S') + " orth " + f.get('type', ' ')  + str(f.find('./oRef'))[9:13], "|", orth_text, "|", A1_1o_(orth_text), "|", "done",  "|", "---", "|")
            else: 
                e.insert(1, f1_copy)
                e.insert(2, f2_copy)  
#                etree.SubElement(f, "lbl", type="time").text = "obsolete"
#                etree.SubElement(f, "prt", type="substitutedBy", target="#CF_newform1 #CF_newform2")
                f.set('status', 'deprecated') # setting attributes of the old form                  
                f.set('corresp', 'CF_newform1 CF_newform2') # setting attributes of the old form
                f1_copy.set('status', 'added')
                f1_copy.set('corresp', form_id)
#                f1_copy.append(etree.Element("ptr", target=form_id))
                f1_copy.attrib.pop('{http://www.w3.org/XML/1998/namespace}id')
                f2_copy.set('status', 'added')
                f2_copy.set('corresp', form_id)
#                f2_copy.append(etree.Element("ptr", target=form_id)) 
                f2_copy.attrib.pop('{http://www.w3.org/XML/1998/namespace}id')
                print ("|", n, "|", form_id, "|", f.findtext('usg', 'S') + " orth " + f.get('type', ' ')  + str(f.find('./oRef'))[9:13], "|", orth_text, "|", A1_1o(orth_text),",", A1_1o_(orth_text), "|", "done",  "|", "---", "|")
#            row = (n, form_id, "orth", orth_text)
#            writer.writerow(row)
    if e.xpath("./form[(@status='deprecated')]") and e.xpath("./form/orth/text()"): 
        print ("|", "entry -->", "|", str((e.attrib).get('{http://www.w3.org/XML/1998/namespace}id', ' ')), "|", "---", "|", "---","|", sorted(list(zip_longest(e.xpath("./form[not(@type='lemma')]/usg/text()"), e.xpath("./form[not(@type='lemma')]/orth/text()"), fillvalue='S'))), "|", "done",  "|", "---", "|")
    if e.xpath("./form[(@status='deprecated')]") and not e.xpath("./form/orth/text()"):       
        print ("|", "entry -->", "|", str((e.attrib).get('{http://www.w3.org/XML/1998/namespace}id', ' ')), "|", "---", "|", "---", "|", sorted(list(zip_longest(e.xpath("./form[not(@type='lemma')]/usg/text()"), e.xpath("./form[not(@type='lemma')]/text()"), fillvalue='S'))), "|", "done",  "|", "---", "|")
tree.write("XML/new_A_2.1.xml", encoding="utf-8", pretty_print=True)
# outfile.close()
