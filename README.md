# Comprehensive Coptic Lexicon - Research Data
The repository “Comprehensive Coptic Lexicon - Research Data” contains the research data related to the dictionary: 

- Project documentation uploaded as PDF-files to the "Code" section and/or written in markdown in "Wiki" section. 
- Released TEI XML Files, XML Schemata and Release Notes.
- Python scripts used in ELT scenarios.

The data in the "Code" section is organized according to the steps, along which the development of the lexicon progressed: 

- Step 0: Encoding Crum as TEI XML
- Step 1: Creation of XML Schema
- Step 2: Matching the TLA Data Model
- Step 3: Standardizing the Spelling of Compounds
- Step 4: Releasing Coptic Lemma List (CLL) V2
- Step 5: Investigating polysemantic entries
- Step 6: Setting standard lemma forms and XML IDs
- Step 7: Releasing Coptic Lemma List (CLL) V2.1
- Step 8: Integrating Greek Loan Words from DDGLC Project
- Step 9: Releasing Comprehensive Coptic Lexicon (CCL) V1
- Step 10: Removing parenthesis (round brackets) from orthographic variants
- Step 11: Adopting the expression of “portmanteau” or “layered” forms
- Step 12: Releasing Comprehensive Coptic Lexicon (CCL) V1.2

The bugtracker of the Comprehensive Coptic Lexicon can be found at KELLIA's dictionary repository: https://github.com/KELLIA/dictionary/issues

Below is a brief description of each step.

## Step 0: Encoding Crum as TEI XML
Summary: 

- Dialectal and stative forms were encoded according to the “exclusivity” principle: e.g. included if the verb was attested in stative but not in infinitive or in Bohairic but not in Sahidic. 
- Status nominalis / status pronominalis forms were not explicitly encoded.
- Verbal compounds included if the meaning could not be deduced from the constituent parts.
- Nominal compounds included.
- No loan words.

## Step 1: Creation of XML Schema
Summary: 

- Coptic Dictionary XML Schema created according to the TEI XML Dictionary Module guidelines.
- Controlled vocabulary for the "part of speech" and "subcategory" elements created, adopting the existing terms to the TLA vocabulary (German).

## Step 2: Matching the TLA Data Model
Summary: 

- Disambiguating the values for gender, number and dialect: separate entries were created in each case.
- Allowing a single "orth" per "form" only (one spelling pro word-form).
- Allowing a single "usg" per "form" only (one dialect entry pro word-form).
- Disambiguating the semantics of "form type="lemma"" tag. Reason: it had different meanings: a) referring to the whole compositum ("ϭⲓⲛⲱⲃϣ"),  b) referrring to a part of a compositum ("ⲉⲓⲛⲉ"). In the latter case "form type="lemma"" was exchanged with "xr type="cf"".

## Step 3: Standardizing the Spelling of Compounds
Summary: 

- Standardizing the spelling of verbal compounds according to the rules outlined in “Verbal compounds.pdf”.
- Standardizing the spelling of nominal compounds according to the rules outlined in “Nominal compounds & other.pdf".
- Inserting cross-references to the parts of the compounds which were corrected.

## Step 4: Releasing Coptic Lemma List (CLL) V2
Summary: 

- A major release containing changes outlined in Steps 1-3.

## Step 5: Investigating Polysemantic Entries
Summary: 

- Investigating polysematic nouns and verbs in Coptic to facilitate the planned integration into the TLA.

## Step 6: Setting Standard Lemma Forms and XML IDs
Summary: 

- Defining a standard form (“Ansetzungsform”) for earch lemma entry.  
- Setting unique entry IDs.
- Setting unique form IDs.
- Special mark-up for "multiword" expressions.

## Step 7: Releasing Coptic Lemma List (CLL) V2.1
Summary: 

- A major release containing changes outlined in Steps 5-6.

## Step 8: Integrating Greek Loan Words from DDGLC Project
Summary: 

- Matching the DDGLC and TLA datamodels.
- Source DDGLC data clean-up and conversion.
- Proofreading the converted data, whiсh necessitated major changes in the source data.
- Conversion and final output of the source data as TLA TEI XML.

## Step 9: Releasing Comprehensive Coptic Lexicon (CCL) V1
Summary: 

- Renaming "Coptic Lemma List" to "Comprehensive Coptic Lexicon", containing Greek loanwords in Coptic.
- Release of three datasets: Version 3 of the BBAW lexicon of Coptic Egyptian (former "Coptic Lemma List"), Version 1 of the DDGLC lexicon of Greek loan words in Coptic and Version 1 of the combined "Comprehensive Coptic Lexicon".
- New TLA TEI XML headers.
- Extended TLA TEI XML Schema.
- Released in Refubium Repository: https://refubium.fu-berlin.de/handle/fub188/24570.

## Step 10: Removing parenthesis (round brackets) from orthographic variants
Summary: 

- Project description can be found [in Wiki](https://github.com/phoenix-mossimo/ccl_rd/wiki/A0-Remove-parenthesis-(round-brackets)-from-orthographic-variants).
- Project changelog can also be found [in Wiki](https://github.com/phoenix-mossimo/ccl_rd/wiki/Changelog-of-the-task-%22Remove-parenthesis%22-(Step-10)).
- The following tasks were completed:
- - Bracket at word beginning and at word end: [Task A1.1](https://github.com/phoenix-mossimo/ccl_rd/wiki/A1.1---Bracket-at-word-beginning-and-at-word-end).
- - Bracket at word beginning but not at word end: [Task A1.2](https://github.com/phoenix-mossimo/ccl_rd/wiki/A1.2-Bracket-at-word-beginning-but-not-at-word-end).
- - Bracket NOT at word beginning and NOT preceded by a white space: [Task A2.1](https://github.com/phoenix-mossimo/ccl_rd/wiki/A2.1-Bracket-NOT-at-word-beginning-and-NOT-preceded-by-a-white-space).
- - Debugging: bracket NOT at word beginning: [Task A2.2](https://github.com/phoenix-mossimo/ccl_rd/wiki/A2.2-Debugging:-bracket-NOT-at-word-beginning).
- - Debugging: the remaining forms containing brackets: [Task A3](https://github.com/phoenix-mossimo/ccl_rd/wiki/A3-The-remaining-forms-containing-brackets).

## Step 11: Adopting the expression of “portmanteau” or “layered” forms
Summary: 

- The expression of grammatical information of “portmanteau” or “layered” forms, which contain two grammatical categories (possessive prefix, designating the possessed item, and possessive suffix, designating the possessor, e.g. ⲛⲁ- (C2353), ⲛⲟⲩ- (C2388), ⲡⲁ- (C2784), ⲡⲟⲩ- (C2787), ⲧⲁ- (C4005), ⲧⲟⲩ- (C11281)) ), was changed. For now a temporary solution was chosen – to relegate some of the grammatical information to the definition text in tag <sense>. The preferred solution is to bring the grammatical encoding in accordance with LEX-0. 
- Project description can be found [in Wiki](https://github.com/phoenix-mossimo/ccl_rd/wiki/B1:-Encode-%E2%80%9Clayered%E2%80%9D-or-%E2%80%9Cportmanteau%E2%80%9D-possessive-forms).
  
## Step 12: Releasing Comprehensive Coptic Lexicon (CCL) V1.2 
Summary:   

- A major release containing changes outlined in Steps 10-11. 
- Additionally: 
- - Unified the location of the written forms to "orth" tag only.
- - Assigned dialect information to Sahidic forms, which, perceived as default, did not have dialect explicitly encoded: "usg type="geo""S"/usg".
- - In line with LEX-0 conventions improved the structure of <sense> element, which now contains a unique ID and a single "cit type="translation"" tag.

## Step 13: Parsing Funk's lexicon
Summary:   

- Singled two dialects out of Funk's lexicon: Bohairic and Akhmimic. 
- Created plain XML files where each element corresponds to a row in Funk.
- Merged elements with property "2" (form) into the corresponding elements with property "1" (lemma) assigning "part of speech" and "sense" values. 
- Exported those as XLSX files for further analysis 
