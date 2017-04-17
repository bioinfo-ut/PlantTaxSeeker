#! /usr/bin/env python3.3
# -*- coding:UTF-8 -*-

#Program info:
#takes multiple fasta file (containing many sequences in fasta format) as input (and option "-w" (by default 32) and
#glistmaker creates k-mer lists for every sequence in the fasta file.

#Command line:
#python3.3 SEQUENCES.FASTA (-w ...)

#Output files are .list files for every sequence from the initial fasta file (glistquery can be used to convert .list -> readable .txt)

import os
import sys
from optparse import OptionParser
from copy import *

["Options:"]
parser=OptionParser()
parser.add_option("-w", "--window", help="Length of the window (bp)", default=32, dest="lenwin")
(options, args)=parser.parse_args()

len_window=int(options.lenwin)

mits_file=open(sys.argv[1])
temporal_file=open("Temp_file.fasta","w")
l=0
for line in mits_file:
    if line.startswith(">"):
        if l>0:
            temporal_file.close()
            os.system("./glistmaker Temp_file.fasta -w "+str(len_window)+" -o Target_list_"+str(l))
            temporal_file=open("Temp_file.fasta","w")
            temporal_file.write(line.strip())
            temporal_file.write("\n")
            l+=1
        else:
            temporal_file.write(line.strip())
            temporal_file.write("\n")
            l+=1
    else:
        temporal_file.write(line.strip())
        
temporal_file.close()
os.system("./glistmaker Temp_file.fasta -w "+str(len_window)+" -o Target_list_"+str(l))
mits_file.close()
