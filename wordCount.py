#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:53:20 2019

@author: adrian
"""

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program
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


#master dictionary
master = {}
#master.setdefault(0) 
master = defaultdict(lambda:0,master)  
    
# attempt to open input file
with open(inputFname, 'r') as inputFile:
    for line in inputFile:
        # get rid of newline characters
        line = line.strip()
        # split line on whitespace and punctuation
        line = re.split('[ \t]', line)
        
        for word in line:
            if len(word) != 0 :
                word = word.lower() 
                master[word]= master[word]+1
            
master  = dict(sorted(master.items()))

for key in master:
    value = master[key]
    print ("%s %s\n" % (key, value))
    
