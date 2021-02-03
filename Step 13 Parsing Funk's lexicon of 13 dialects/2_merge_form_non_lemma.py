# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:20:02 2016
@author: Max

"""
'''

Task: each entry should have ONLY ONE <form type="lemma"> 

Rules: 

'''
import xml.etree.ElementTree as ET
import glob
from copy import deepcopy
file_number=0

for file in glob.glob("XML\Bohairic.xml"):
    file_number = file_number + 1
    file_name = 'XML_out/{:03d}.xml'.format(file_number)       

    tree = ET.parse(file)
    base = tree.getroot()    # "root" is everything starting with <text>
    entries = base.findall("./entry")
    first_entry = base.find("./entry")
    first_entry_id = (first_entry.attrib).get('id')
    print (first_entry)
    n = 0
  
    for e in base.iter('entry'): 
        entry_id = str((e.attrib).get('id',' '))
        entry_type = str((e.attrib).get('type'))                 
    for e in base.iter('entry'): 
        entry_id = str((e.attrib).get('id',' '))
        entry_type = str((e.attrib).get('type'))                 
        if entry_type != "1":
            print (entry_id)
            forms = e.findall("./form") 
            for f in forms:   
                orth_attribute = f.find('./orth').attrib['target_entry_id']
                try:
                    target_entry = base.find("./entry[@id='{}']".format(orth_attribute))                    
                    current_form = deepcopy(f)                    
                    target_entry.insert(1, current_form)                   
                except: 
                    print ("Form belonging to the entry", entry_id, "WAS NOT assigned to the entry", orth_attribute)                      
                    current_form = deepcopy(f)                         
                    first_entry.insert(1, current_form)                                                         
#           base.remove(e)
    tree.write(file_name, encoding="utf-8")                
                    


          

              
      
      






