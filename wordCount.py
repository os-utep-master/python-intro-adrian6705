#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Adrian Sosa
"""

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
from collections import defaultdict

# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

inputFname = sys.argv[1]
outputFname = sys.argv[2]

#make sure text files exist
if not os.path.exists(inputFname):
    print ("text file input %s doesn't exist! Exiting" % inputFname)
    exit()


#master dictionary, all word counts set to begin at 0
master = {}
master = defaultdict(lambda:0,master)  
    
# attempt to open input file
with open(inputFname, 'r') as inputFile:
    for line in inputFile:
        # get rid of newline characters
        line = line.strip()
        # remove non-letter characters
        line = re.sub('[!@#$-:,;"]', ' ', line)
        # split line on whitespace and punctuation
        line = re.split('[ \t]', line)
        
        for word in line:
            if len(word) != 0 :
                word = word.lower() 
                master[word]= master[word]+1
                
# sort words in dictionary          
master  = dict(sorted(master.items()))

with open(outputFname, 'w') as outputFile:    
    for key in master:
        value = master[key]
        outputFile.write ("%s %s\n" % (key, value))
        
    outputFile.close()
    
