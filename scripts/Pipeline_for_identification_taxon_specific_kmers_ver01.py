#! /usr/bin/env python3.3
# -*- coding:UTF-8 -*-

#Programmer: Kairi Raime
#Program takes 1. target taxon sequences (as one FASTA file) and 2. Nontarget taxons sequences (as one FASTA file) as inputs,
#creates k-mer lists(default k value 32), compares kmers lists of target and nontarget taxons and
#as a result creates a list of target taxon specific k-mers as .list file and also as .txt file (includes k-mers' sequences and frequences)

#This pipeline of program needs for executing following programs: python, Glistmaker_multiple_runner.py and different GenomeTester4 programs: glistmaker, glistcompare, glistquery, MakeUnion.pl.   
#Example of command line arguments:
#python3.3 ....py Targets.fasta Nontargets.fasta (-w ...) (-f...)

#Output file contains k-mers (by default with length 32, option "-w") that are present in specified number of target sequences (by default at least 1, option "-f")
#but none of the nontarget sequences.

#NB Working directory must not contain files with ".list" extension or directories with name "union_ ..."!!!

import os
import sys
import os.path
from optparse import OptionParser
from copy import *

["Options:"]
parser=OptionParser()
parser.add_option("-w", "--window", help="Length of the window (bp)", default=32, dest="lenwin")
parser.add_option("-f", "--frequency", help="The minimum number of sequences that should contain every specific kmers", default=1, dest="freq")
(options, args)=parser.parse_args()

len_window=int(options.lenwin) 
kmer_freq=int(options.freq)

print("Program starts ...")

#Creating k-mer lists from one (multiple) FASTA file of target sequences:
targets_file=open(sys.argv[1])
temporal_file=open("Temp_file.fasta","w")
l=0
for line in targets_file:
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
targets_file.close()
print("Target(s) kmers done!")

#Changing all frequency values in targets lists to 1(depending on the location k-mers frequency may be 1 or 2):
i=1
while os.path.isfile("Target_list_"+str(i)+"_"+str(len_window)+".list"):
    os.system("./glistcompare Target_list_"+str(i)+"_"+str(len_window)+".list Target_list_"+str(i)+"_"+str(len_window)+".list -i -r 1 -o Target_list_"+str(i)+"_corrfreq")
    os.remove("Target_list_"+str(i)+"_"+str(len_window)+".list")
    i+=1
if i>1:
    print("Target kmers' frequencies has modified to 1!")
else:
    print("Target kmers' frequencies modifying FAILED!!!")

#Finding the union of target k-mer lists (output: "union_..._union.list"):
if l>1:
    os.system("./MakeUnion.pl *.list")
    print("Universal targets' kmers selected!")
    #Finding and removing k-mers that are not represented in specified number of target sequences (by default: removing k-mers that are represented in only 1 sequences - individual specific k-mers):
    os.system("./glistcompare union_"+str(len_window)+"_union.list union_"+str(len_window)+"_union.list -i -r first -c "+str(kmer_freq)+" -o union_"+str(len_window)+"_union_freq"+str(kmer_freq))
    print("Target kmers with frequency more than "+str(kmer_freq)+" selected!")
else:
    if l==1:
        os.system("mv Target_list_1_corrfreq_"+str(len_window)+"_intrsec.list union_"+str(len_window)+"_union_freq"+str(kmer_freq)+"_"+str(len_window)+"_intrsec.list")
    else:
        print("Couldn´t find any target sequences!")
#Creating k-mer lists of nontarget taxons:
nontargets_file_name=str(sys.argv[2])
os.system("./glistmaker "+nontargets_file_name+" -w "+str(len_window)+" -o Nontarget_kmers")
print("Nontargets kmers done!")

#Finding target taxon specific k-mers (output: Specific_kmers_32_0_diff1.list):
os.system("./glistcompare union_"+str(len_window)+"_union_freq"+str(kmer_freq)+"_"+str(len_window)+"_intrsec.list Nontarget_kmers_"+str(len_window)+".list -d -o Specific_kmers")
print("Specific target kmers selected!")

#Target taxon specific k-mers as .txt file:
os.system("./glistquery Specific_kmers_"+str(len_window)+"_0_diff1.list > Specific_kmers_"+str(len_window)+".txt")
print("Specific kmers are visible in textfile now!")

#Deleting unnecessary files ...
os.remove("Temp_file.fasta")
os.remove("union_"+str(len_window)+"_union.list")
os.remove("union_"+str(len_window)+"_union_freq"+str(kmer_freq)+"_"+str(len_window)+"_intrsec.list")
os.remove("Nontarget_kmers_"+str(len_window)+".list")
for k in range(l):
    os.remove("Target_list_"+str(k+1)+"_corrfreq_"+str(len_window)+"_intrsec.list")
os.system("rm -r union_*")
os.system("mv Specific_kmers_"+str(len_window)+"_0_diff1.list Specific_kmers_"+str(len_window)+".list")


print("Done!")
