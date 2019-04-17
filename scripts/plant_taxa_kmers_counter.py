#! /usr/bin/env python3.3
# -*- coding:UTF-8 -*-

#Programmer: Kairi Raime
#Program:
#1. Input files: target taxa specific k-mers list (as txt file) and FASTQ file that are used for counting k-mers from.
#2. creating gmer_counter input-file (k-mers database) from target taxon k-mers list TEXT-file (.txt) (glistquery output file (GenomeTester4 toolkit))
#3. searches and counts k-mers in given FASTQ file(s).
#Commandline:
#python3.3 plant_taxa_kmers_counter.py Target_specific_kmers.txt Data.fastq (-f 2)

import os
import sys
import os.path
from optparse import OptionParser
from copy import *

["Options:"]
parser=OptionParser()
parser.add_option("-f", "--frequency", help="The minimum allowed k-mer frequency in sequencing data", default=1, dest="freq")
(options, args)=parser.parse_args()
 
kmer_freq=int(options.freq)

print("")
print("Program starts ...")

#part I
#Creating k-mers database file (inputfile for gmer_counter) from glistquery (GenomeTester4 Toolkit) output file
K_seq=[] #Kmer sequences as list of strings
K_file=open(sys.argv[1]) #K-mers file as .txt (outputfile of glistquery)
counter=0

for line in K_file:
    if not line.startswith("NUnique") and not line.startswith("NTotal"):
        line_cuts=line.split("\t")
        K_seq.append(line_cuts[0].strip())
        counter+=1
    else:
        if line.startswith("NUnique"):
            line_cuts=line.split("\t")
            nr=line_cuts[1].strip()
K_file.close()

db_file=open("Kmers_database.txt","w")
db_file.write("Targettaxon"+"\t")
db_file.write(str(nr)+"\t")

for i in range(len(K_seq)):
    db_file.write(K_seq[i])
    db_file.write("\t")
db_file.close()
print("")
print(str(counter)+" taxa specific k-mers in database")
print("")

#part II
#Counting database kmers in fastq files ...
Data_file=sys.argv[2] #Data file - e.g sequencing raw read of food samples as FASTQ format file file
namecuts=Data_file.split(".")
print("Counting database kmers with frequency at least "+str(kmer_freq)+" in "+Data_file+" ...")
os.system("./gmer_counter -db  Kmers_database.txt "+Data_file+" > Kmers_database_"+namecuts[0]+".txt")

# Counting and printing only kmers count with specified frequency in FASTQ file:
count_file=open("Kmers_database_"+namecuts[0]+".txt")
for line in count_file:
    line_cuts=line.split("\t")
    counter=0
    for k in range(2,len(line_cuts)):
        if int(line_cuts[k])>(kmer_freq-1): # if cutoff value other than >=1 it is nessecary to change this, for example ">9" if frequencies with at least 10 is needed to see
            counter+=1
print("The number of kmers in "+namecuts[0]+".txt: "+str(counter)) # The number of kmers with frequency value at least 1
count_file.close()
print("")
print("program has finished!")


