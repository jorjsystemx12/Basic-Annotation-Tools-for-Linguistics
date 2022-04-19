#Utilize SpaCy, load the best-model and calculate top entries for selected POS tags

#Import all needed tools
import os
import spacy
import sys
import re
import glob
from collections import Counter

#open directory
os.chdir('Alpine_Journal')

#Load the spacy language model of choice - our best-model is loaded in here
nlp = spacy.load('en_core_web_sm')

#Read the collection of file (alpine full collection):
#Enter the readfile here and read as string:
for file in os.listdir():
    if file.endswith('.txt'):
        with open(file, 'r', encoding='utf-8') as f:
            fullpack = f.read()
            fullpack = fullpack.replace('\n', '')
            #print(fullpack)
    
            #Enter the string text here in spacy nlp processor
            doc = nlp(fullpack)

            #Collect all tokenized words into this list
            all_words = [token for token in doc if not token.is_stop and not token.is_punct]
            print(all_words)

            #1 PERSON:
            persons = [token.text
                     for token in all_words
                     if token.pos_ == "PERSON"]
            
            #2 GPE:
            gpes = [token.text
                     for token in all_words
                     if token.pos_ == "GPE"]
                         
            #3 DATE:
            dates = [token.text
                     for token in all_words
                     if token.pos_ == "DATE"]

            #4 MOUNTAINS:
            mountains = [token.text
                     for token in all_words
                     if token.pos_ == "MNTN"]

            #5 WATER:
            waters = [token.text
                     for token in all_words
                     if token.pos_ == "WATER"]
                         
            #6 ROCK:
            rocks = [token.text
                     for token in all_words
                     if token.pos_ == "ROCK"]
            

            # top 10 most common person tokens
            person_freq = Counter(persons)
            common_ten_persons = person_freq.most_common(10)
            print(common_ten_persons)

            # top 10 most common gpe tokens
            gpe_freq = Counter(gpes)
            common_ten_gpe = gpe_freq.most_common(10)
            print(common_ten_gpe)

            # top 10 most common date tokens
            date_freq = Counter(dates)
            common_ten_date = date_freq.most_common(10)
            print(common_ten_date)

            # top 10 most common mountain tokens
            mountain_freq = Counter(mountains)
            common_ten_mountain = mountain_freq.most_common(10)
            print(common_ten_mountain)

            # top 10 most common water tokens
            water_freq = Counter(waters)
            common_ten_water = water_freq.most_common(10)
            print(common_ten_water)

            # top 10 most common rock tokens
            rock_freq = Counter(rocks)
            common_ten_rock = rock_freq.most_common(10)
            print(common_ten_rock)

