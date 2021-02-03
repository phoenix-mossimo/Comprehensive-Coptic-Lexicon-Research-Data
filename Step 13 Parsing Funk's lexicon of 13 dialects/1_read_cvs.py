# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:09:04 2018

@author: Max
"""

import xml.etree.ElementTree as ET
import csv
import re

body = ET.Element("body")
text = ET.SubElement(body, "text")

reader = csv.DictReader(open('CSV/Bohairic_in.csv', newline='', encoding='utf-8'), delimiter=',')
for row in reader:
    type = row['TYPE'].strip()
    cd_mot = row['CD_MOT'].strip()
    mot = row['MOT'].strip()
    entry = ET.SubElement(text, "entry")
    entry.set ('type', type)
    entry.set ('id', cd_mot)
    
    if type == "1": 
        form_lemma = ET.SubElement(entry, "form", type="lemma")
        gram_grp = ET.SubElement(entry, "gramGrp")    
        sense = ET.SubElement(entry, "sense")        
        if ' "' in  mot: 
            ET.SubElement(form_lemma, "orth").text = re.findall('(.+?)\"', mot)[0]            
#            ET.SubElement(sense, "cit", type="translation", xmllang = "en").text = re.findall('\s+\".+\"', mot)[0]
            ET.SubElement(sense, "cit", type="translation", xmllang = "en").text = re.findall('\s+\".+', mot)[0]
            ET.SubElement(gram_grp, "pos", type="pos_1").text = row['pos_1'].strip()       
        elif ' (' in  mot:
            ET.SubElement(gram_grp, "pos", type="pos_1").text = row['pos_1'].strip()            
            ET.SubElement(gram_grp, "pos", type="mot").text = re.findall('\s+\(.+\)', mot)[0]
            ET.SubElement(form_lemma, "orth").text = re.findall('(.+?)\(', mot)[0]
            ET.SubElement(sense, "cit", type="translation", xmllang = "en")
        else: 
            ET.SubElement(form_lemma, "orth").text = row['MOT'].strip()
            ET.SubElement(gram_grp, "pos", type="pos_1").text = row['pos_1'].strip()
            ET.SubElement(sense, "cit", type="translation", xmllang = "en")
    else:                
        relations = "{} {} {} {} {} {} {} {} {} {}".format(*[row[column] for column in ['id_1', 'id_2', 'id_3', 'id_4', 'id_5', 'id_6', 'id_7', 'id_8', 'id_9', 'id_10']])
        for r in relations.split():
            form_non_lemma = ET.SubElement(entry, "form", source_entry_id ="{}".format(cd_mot)) 
            ET.SubElement(form_non_lemma, "orth", target_entry_id = r).text = row['MOT'].strip()

tree = ET.ElementTree(text)
tree.write('XML/Bohairic.xml', encoding='utf-8')
