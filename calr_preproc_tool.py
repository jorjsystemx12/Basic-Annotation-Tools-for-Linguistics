#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# preprocessing XML to .txt program

# University of Zurich
# Department of Computational Linguistics
# Authors: Mirela Vasilica-Ratoi & George Yong

#import needed
import os
import re
import sys
import codecs
import xml.etree.ElementTree as ET

#directory to the folder of all alpine journals:
os.chdir('Alpine_Journal')
for file in os.listdir():
    #if it ends with .xml, then proceed
    if file.endswith('.xml'):
        #and the file does not have -ner
        if not file.endswith('-ner.xml'):

            #Extract files as input:
            tree = ET.parse(file)
            root = tree.getroot()

            #Write the file in .txt:
            extension = '_convert.txt'
            file_name_chunk = file[:-4]
            #the name of the converted file will end with _convert.txt
            finalized = file_name_chunk + extension
            #write new file to place converted text
            with open(finalized, 'w', encoding = 'utf-8') as f:
            #print(root)
                for article in root.findall('article'):
                    for division in article.findall('div'):
                        for sentence in division.findall('s'):
                            sent = ''
                            for word in sentence.findall('w'):
                                sent = sent + word.text + ' '
                            #print(sent)
                            f.write(sent + '\n')
            