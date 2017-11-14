#! /usr/bin/env python3.3
# -*- coding:UTF-8 -*-

#Programmer: Kairi Raime
#Program takes target taxon kmers list file and 3 or more nontarget taxon fastq (e.g SRA raw reads) or fasta (e.g. assembled genome sequence) files as input files.
#By default the expected number of nontarget taxa files is 3, kmer length 32 and frequency of kmers in nontargets that are filtered out from target kmers list is at least 10 (suitable for using fastq files of raw reads from SRAsequences).
#Program creates new file that contains only taxon-specific kmers (kmers that are in targetlist and are not in nontarget fastq_files with at least given frequency (by default: at least 10).
#Commandline:
#python3.3 ... .py Target.list Nontarget1.fastq Nontarget2.fastq Nontarget3.fastq ... (-n ...) (-w ..) (-f ...)
#An example of commandline using 3 nontarget taxa files, kmer length 32 and kmer frequency cutoff 10 for filtering (default values):
#python3.3 ... .py Target.list Nontarget1.fastq Nontarget2.fastq Nontarget3.fastq -n 3 -w 32 -f 10

import os
import sys
import os.path
from optparse import OptionParser
from copy import *

["Options:"]
parser=OptionParser()
parser.add_option("-n", "--nontargets", help="The number of nontargets for filtering", default=3, dest="nontar")
parser.add_option("-w", "--window", help="Length of window/the lenght of kmers (bp)", default=32, dest="lenwin")
parser.add_option("-f", "--cutoff", help="The kmer frequency cutoff (only kmers from nontarget sequences with at least given frequency cutoff will be filtered out from target kmer list)", default=10, dest="fcutoff")

(options, args)=parser.parse_args()

nr_nontargets=int(options.nontar)
len_window=int(options.lenwin)
freq_cutoff=int(options.fcutoff)

print("Starting ...")

targetlist_file=str(sys.argv[1])
targetfile_cut=targetlist_file.split(".")

#Creating kmers list files from nontarget fastq files ..."
print("The number of nontargets: "+str(nr_nontargets))
nontarget_fastqs=[]
for i in range(nr_nontargets):
    nontarget=str(sys.argv[i+2])
    nontarget_fastqs.append(nontarget)

nontarget_lists=[]
for j in range(nr_nontargets):
    os.system("./glistmaker "+nontarget_fastqs[j]+" -w "+str(len_window)+" -o nontarget"+str(j+1))
    nontarget_lists.append("nontarget"+str(j+1)+"_32.list")


#Filtering out only kmers  from SRA that are with given frequency (default value: at least 10):
for k in range(nr_nontargets):
    os.system("./glistcompare "+nontarget_lists[k]+" "+nontarget_lists[k]+" -i -r second -c "+str(freq_cutoff)+" -o Nontarget"+str(k+1)+"_cutoff10")

print("Filtering nonspecific kmers ...")
#Filtering k-mers that are in nontarget kmers lists ...
 
os.system("./glistcompare "+targetlist_file+" Nontarget1_cutoff10_32_intrsec.list -d -o "+targetfile_cut[0]+"_not_in_nontarget1")
if nr_nontargets>1:
    for l in range(nr_nontargets-1):
        os.system("glistcompare "+targetfile_cut[0]+"_not_in_nontarget"+str(l+1)+"_32_0_diff1.list Nontarget"+str(l+2)+"_cutoff10_32_intrsec.list -d -o "+targetfile_cut[0]+"_not_in_nontarget"+str(l+2))

    print("Removing files ...")
    for m in range(nr_nontargets):
        os.remove("Nontarget"+str(m+1)+"_cutoff10_32_intrsec.list")
        os.remove("nontarget"+str(m+1)+"_32.list")

    for n in range(nr_nontargets-1):
        os.remove(targetfile_cut[0]+"_not_in_nontarget"+str(n+1)+"_32_0_diff1.list")
else:
    if nr_nontargets==1:
        os.remove("Nontarget1_cutoff10_32_intrsec.list")
        os.remove("nontarget1_32.list")
    else:
        print("Nontarget fastq files have not given!!!")
        
os.system("./glistquery "+targetfile_cut[0]+"_not_in_nontarget"+str(nr_nontargets)+"_32_0_diff1.list > "+targetfile_cut[0]+"_not_in_nontarget"+str(nr_nontargets)+"_32_0_diff1.txt")


print("program has finished!")
