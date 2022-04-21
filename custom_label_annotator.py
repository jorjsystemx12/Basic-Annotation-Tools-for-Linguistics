#Utilize SpaCy, load the best-model and calculate top entries for selected POS tags

#Import all needed tools
import os
import spacy
import sys
import re
import glob
from collections import Counter
nlp = spacy.load('./sac_ner/model-best')
nlp.max_length = 1500000
#open directory
os.chdir('Alpine_Journal')



#Read the collection of file (alpine full collection):
#Enter the readfile here and read as string:

persons=[]
gpes=[]
dates= []
mountains = []
waters = []
rocks= []
for file in os.listdir():
    if file.endswith('.txt'):
        with open(file, 'r', encoding='utf-8') as f:
            fullpack = f.read()
            fullpack = fullpack.replace('\n', '')
            #print(fullpack)
    
            #Enter the string text here in spacy nlp processor
            doc = nlp(fullpack)
            for ent in doc.ents:
                if ent.label_ == "PERSON":
                    persons.append(ent.text)
                if ent.label_ == "GPE":
                    gpes.append(ent.text)
                if ent.label_ == "DATE":
                    dates.append(ent.text)
                if ent.label_ == "MNTN":
                    mountains.append(ent.text)
                if ent.label_ == "WATER":
                    waters.append(ent.text)
                if ent.label_ == "ROCK":
                    rocks.append(ent.text)


            # top 10 most common person tokens
person_freq = Counter(persons)
common_ten_persons = person_freq.most_common(10)
print(f'PERSON: {common_ten_persons}') # added

            # top 10 most common gpe tokens
gpe_freq = Counter(gpes)
common_ten_gpe = gpe_freq.most_common(10)
print(f'GPE: {common_ten_gpe}')

            # top 10 most common date tokens
date_freq = Counter(dates)
common_ten_date = date_freq.most_common(10)
print(f'DATES: {common_ten_date}')

            # top 10 most common mountain tokens
mountain_freq = Counter(mountains)
common_ten_mountain = mountain_freq.most_common(10)
print(f'Mountains: {common_ten_mountain}')

            # top 10 most common water tokens
water_freq = Counter(waters)
common_ten_water = water_freq.most_common(10)
print(f'WATER: {common_ten_water}')

            # top 10 most common rock tokens
rock_freq = Counter(rocks)
common_ten_rock = rock_freq.most_common(10)
print(f'ROCKS: {common_ten_rock}')

