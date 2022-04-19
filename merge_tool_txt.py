#Merge all the text files into one big text file for the evaluation:
#Import all needed tools
import sys
import re
import glob

#Read all the files that end with .txt
file_collect = glob.glob("*.txt")

#Create a new file that contains all the text:
with open("BAC_all_1969_to_2008.txt", "wb") as output:
    #For each individual file
    for f in file_collect:
        with open(f, "rb") as infile:
            #Write through the content
            output.write(infile.read())