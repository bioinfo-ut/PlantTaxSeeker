#! /usr/bin/env python3.3
# -*- coding:UTF-8 -*-

#Program info:
#1. creating k-mer lists(default k value 32) from target taxon sequences (as one FASTA file)
#2. finding k-mers that are present in specified number of target sequences
#3. creating k-mer lists from nontarget taxons' sequences (as one FASTA file)
#4. comparing lists of target and nontarget taxons and
#5. creating a list of target taxon specific k-mers as .list file and also as .txt file (includes k-mers' sequences and the frequency values of the k-mers)

#This pipeline of program needs for executing following programs:
#python(3. ...), Glistmaker_multiple_runner.py and GenomeTester4 programs: glistmaker, glistcompare, glistquery, MakeUnion.pl.   

#Command line: python3.3 TARGETS.FASTA NONTARGETS.FASTA (-w ...) (-f...)
#   -w  ... k-mer length, value of k (default value: 32)
#   -f  ... the minimum number of target sequences that should contain target-taxon-specific k-mers (default value: >= 2)

#Output file (.txt): contains k-mers (by default with length 32, option "-w") that are present in specified number of target sequences (by default at least 2, option "-f")
#but none of the nontarget sequences.

#NB Working directory should not contain other .list files!

import os
import sys
import os.path
from optparse import OptionParser
from copy import *

["Options:"]
parser=OptionParser()
parser.add_option("-w", "--window", help="Length of the window (bp)", default=32, dest="lenwin")
parser.add_option("-f", "--frequency", help="The minimum number of target sequences that should contain every specific kmers", default=2, dest="freq")
(options, args)=parser.parse_args()

len_window=int(options.lenwin) 
kmer_freq=int(options.freq)

print("Program starts ...")

#Creating k-mer lists from one multiple FASTA file of target sequences:
targets_file_name=str(sys.argv[1])
os.system("python Glistmaker_multiple_runner.py "+targets_file_name+" -w "+str(len_window))
print("Targets kmers done!")

#Changing all frequency values in targets lists to 1(depending on the location k-mers frequency may be 1 or 2):
i=1
while os.path.isfile("Target_list_"+str(i)+"_"+str(len_window)+".list"):
    os.system("./glistcompare Target_list_"+str(i)+"_"+str(len_window)+".list Target_list_"+str(i)+"_"+str(len_window)+".list -i -r 1 -o Target_list_"+str(i)+"_corrfreq")
    os.remove("Target_list_"+str(i)+"_"+str(len_window)+".list")
    i+=1
if i>1:
    print("Target kmers frequencies has modified to 1!")
else:
    print("Target kmers frequencies modifying FAILED!!!")

#Finding the union of target k-mer lists (output: "union_32_union.list"):
os.system("./MakeUnion.pl *.list")
print("Universal targets' kmers selected!")

#Finding and removing k-mers that are not represented in specified number of target sequences (by default: removing k-mers that are represented in 1 sequences - individual specific k-mers):
os.system("./glistcompare union_"+str(len_window)+"_union.list union_"+str(len_window)+"_union.list -i -r first -c "+str(kmer_freq)+" -o union_"+str(len_window)+"_union_freq"+str(kmer_freq))
print("Target kmers with frequency more than "+str(kmer_freq)+" selected!")
    
#Creating k-mer lists of nontarget taxons:
nontargets_file_name=str(sys.argv[2])
os.system("./glistmaker "+nontargets_file_name+" -w "+str(len_window)+" -o Nontarget_kmers")
print("Nontargets kmers done!")

#Finding target taxon specific k-mers (output: Specific_kmers_32_0_diff1.list):
os.system("./glistcompare union_"+str(len_window)+"_union_freq"+str(kmer_freq)+"_"+str(len_window)+"_intrsec.list Nontarget_kmers_"+str(len_window)+".list -d -o Specific_kmers")
print("Specific target kmers selected!")

#Target taxon specific k-mers as .txt file:
os.system("./glistquery Specific_kmers_"+str(len_window)+"_0_diff1.list > Specific_kmers.txt")
print("Specific kmers are visible in textfile now!")

print("Done!")
