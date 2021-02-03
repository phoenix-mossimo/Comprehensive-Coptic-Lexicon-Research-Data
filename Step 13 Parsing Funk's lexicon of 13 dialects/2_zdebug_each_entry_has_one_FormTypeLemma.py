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
file_number=0
lemma_number = 0

for file in glob.glob("XML_out\*.xml"):
    file_number = file_number + 1

    tree = ET.parse(file)
    root = tree.getroot()    # "root" is everything starting with <text>
    
    entry_number = 0
    n = 0
    
# PART 1: getting all entries and the value of the entry attribute "type"

    for e in root.iter('entry'):    # Element.iter() finds all elements with a given tag ('entry')
        entry_number = entry_number + 1 # entry_number counts entries in one file
        lemma_number = lemma_number + 1 # lemma_number counts entries in all files 
        entry_attribute = str((e.attrib).get('type',' ')) # gets the value of the attribute "type" of the given entry "y"; default value is " " instead of "None"
  
# PART 2: getting all information, related to the form

        forms = e.findall("./form") # Element.findall() finds only elements with a tag which are direct children of the current element.        
        first_form = e.find("./form") # Element.find() finds the first child with a particular tag
        lemma_form = e.find("./form[@type='lemma']") # Element.find() finds the first child with a particular tag and an attribute "type='lemma'"
        form_number = 0
        all_forms = ""
        form_attributes = []
        for f in forms:   
            form_number = form_number + 1
# get attribute
            form_attribute = ' ' # in case form has no attributes, we don't want to have "None"
            form_attribute = str((f.attrib).get('type', ' ')) # gets the value of the attribute "type" of the given form "f"; default value is " " instead of "None"
            form_attributes.append(form_attribute)
# get text in "form" tag            
            form = str(f.text)     # "i.text" gets text from the current element (i). "i.findtext('usg')" gets text from the child element  'usg'      
            form =form.strip()                    
# get dialect
            dialect = str(f.findtext('usg', 'S')) #finds the text of the child element "usg" of the "i"; default value is "S"
# get orths
            orths = f.findall("./orth")    # Element.findall() finds only elements with a tag which are direct children of the current element.   
            orth_number = 0     
            all_orths = ""        
            for o in orths:         
                orth_number = orth_number + 1            
                orth =str(o.text) 
                orth = str(orth)
                x = orth + " (" + dialect + ")"
                all_orths = all_orths + x
# get GramGrp, which is in "form" 
            GramGrp = f.findall("./gramGrp") # "i" becomes the root, so I can look for all GramGrp in forms             
            gender_form = " " # this is necessary so that the value from the previous loop is not transmitted to the next one
            number_form = " "
            pos_form = " "
            for g in GramGrp:     
                gender_form = str(g.findtext('gen', ' '))
                number_form = str(g.findtext('number', ' '))
                pos_form = str(g.findtext('pos', ' '))
            g_form = ' : ' + str(pos_form) + ' '+ str(gender_form) + ' ' + str(number_form)           
# saving all information related to all forms
            ff = 'Form ' + str(form_number) + ' ' +  form_attribute + ': ' + form + all_orths + g_form + '\n'
            all_forms = all_forms + ff

# getting grammatical information related to the entry  
        GramGrp = e.findall("./gramGrp") # "y" becomes the root, so I can look for all GramGrp in entry)             
        gender = " "
        number = " "
        pos = " "
        for g_e in GramGrp:    
            pos = str(g_e.findtext('pos', ' '))            
            gender = str(g_e.findtext('gen',' '))
            number = str(g_e.findtext('number', ' '))
        g_entry = str(pos) + ' '+ str(gender) + ' ' + str(number) + '\n'     
         
        senses = e.findall("./sense") # look for all senses in entry
        sense_number = 0
        all_senses = ""        
        for s in senses: 
            sense_number = sense_number + 1
            cit = s.findall("./cit") # produces a list of all <cits> in <sense>
            for x in cit:  # looking through the list 
                bibl = str(x.findtext('bibl'))
                if ((x.attrib).get('xmllang')) == 'de':            
                    quote_de = str(x.findtext('quote'))
                    def_de = str(x.findtext('def'))                   
                    if quote_de == "None":                        
                        quote_de = def_de
                if ((x.attrib).get('xmllang')) == 'en':        
                    quote_en = str(x.findtext('quote'))
                    def_en = str(x.findtext('def'))
                    if quote_en == "None":                        
                        quote_en = def_en                    
                if ((x.attrib).get('xmllang')) == 'fr':
                    quote_fr = str(x.findtext('quote'))
                    def_fr = str(x.findtext('def'))
                    if quote_fr == "None":                        
                        quote_fr = def_fr   
            citation = "DE: " + quote_de + " EN: " + quote_en + " FR: " + quote_fr + " (" + bibl + ")" + '\n'
            s = str(sense_number) + ': ' + citation 
            all_senses = all_senses + s
        lemma_forms_number = 0
        for z in form_attributes: 
            if z == "lemma": 
                lemma_forms_number = lemma_forms_number + 1
            if lemma_forms_number > 1: 
                print (quote_de)



          

              
      
      






