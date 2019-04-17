# AN EXAMPLE OF IDENTIFICATION <i>S. LYCOPERSICUM</i> SPECIFIC <i>K</i>-MERS   
In this example we are identifying <i>S. lycopersicum</i> specific <i>k</i>-mers with length 32 bases that are present in at least 2 of 5 <i>S. lycopersicum</i> chloroplast genome and none of the given 1714 nontarget taxa chloroplast genome.
We also filter out <i>k</i>-mers that are present in <i>S. tuberosum</i> or <i>S. pimpinellifolium</i> whole sequencing raw reads with frequency at least 10. Sequencing reads are downloaded from NCBI SRA database.
  
Before you can start, you need to:
* a) download PlantTaxSeeker repository containing bins, scripts and readme files from [Github](https://github.com/bioinfo-ut/PlantTaxSeeker)  
* b) move to the folder "example"   
* c) download <i>S. lycopersicum</i> and nontarget taxa chloroplast genome sequences as FASTA format files, and also sequencing data of 4 samples as FASTQ-format files from [HERE](http://www.bioinfo.ut.ee/PlantTaxSeeker/).    
    
Make sure you have enough space for storing these files. FASTA files that are used in this example are ca  255 MB. The FASTQ files are ca 157 GB unpacked. The results files containing <i>k</i>-mers´ lists are ca 100 KB.    
FASTA files contain 5 <i>S. lycopersicum</i> and 1714 nontarget taxa chloroplast genome sequences. FASTQ files contain whole genome sequencing raw reads of 4 samples of <i>S. tuberosum</i> or <i>S. pimpinellifolium</i> (NCBI SRA accession numbers ERR418080, SRR1608100, SRR2069941 and SRR1481624).

Use following command lines to perform the example analysis ("bash test.sh" downloads FASTA and FASTQ files, moves bins and scripts needed for analysis to the folder "example" and executes scripts):
```  
git clone https://github.com/bioinfo-ut/PlantTaxSeeker/
cd PlantTaxSeeker/example/
bash test.sh
```  
   
The 4 results files contain the lists of <i>S. lycopersicum</i> specific <i>k</i>-mers before ("Specific_kmers_32.txt", "Specific_kmers_32.list) and after additional filtering. <i>K</i>-mers´ lists are given as binary files (enables additional operations using GenomeTester4 programs) and also as human readable TXT files.  
