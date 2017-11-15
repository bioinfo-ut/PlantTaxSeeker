# AN EXAMPLE OF IDENTIFICATION <i>S. LYCOPERSICUM</i> SPECIFIC <i>K</i>-MERS   
In this example we are identifying <i>S. lycopersicum</i> specific <i>k</i>-mers with length 32 bases that are present in at least 2 of 5 <i>S. lycopersicum</i> chloroplast genome and none of the given 1714 nontarget taxa chloroplast genome.
We also filter out <i>k</i>-mers that are present in <i>S. tuberosum</i> or <i>S. pimpinellifolium</i> whole sequencing raw reads with frequency at least 10. Sequencing reads are downloaded from NCBI SRA database.

Before you can start, you need to a) download GenomeTester4 binaries and all the scripts (from [Github](https://github.com/bioinfo-ut/PlantTaxSeeker)) b) download <i>S. lycopersicum</i> and nontarget taxa chloroplast genome sequences as FASTA format files, and also sequencing data of 4 samples as FASTQ-format files from [HERE](http://www.bioinfo.ut.ee/PlantTaxSeeker/).  
Make sure you have enough space for storing these files. FASTA files that are used in this example are ca  255 MB. The FASTQ files are ca 157 GB unpacked. The results files containing <i>k</i>-mers´ lists are ca 100 KB.  

## To identify <i>S. lycopersicum</i> specific <i>k</i>-mers , use the following command:  

```
>python3.3 identification_of_taxon_specific_kmers.py Solanum_lycopersicum_complete_chl_genomes_07Jan16.fasta Nontarget_taxa_complete_chl_genomes_07Jan16.fasta -w 32 -f 2   
```
	  
<i>Input files:</i> 
* Solanum_lycopersicum_complete_chl_genomes_07Jan16.fasta  (contains 5 chloroplast genome sequences) 
* Nontarget_taxa_complete_chl_genomes_07Jan16.fasta   (contains 1714 chloroplast genome sequences)
  
<i>Output files:</i>  
* The list of <i>S. lycopersicum</i> specific <i>k</i>-mers (the count of <i>k</i>-mers and sequences) as binary file  
* The list of <i>S. lycopersicum</i> specific <i>k</i>-mers as human readable TXT file  
  
## For additional filtering use the following command:  
```
>python3.3 filtering_with_nontargets.py Specific_kmers_32.list ERR418080.fastq SRR1608100.fastq SRR2069941.fastq SRR1481624.fastq -w 32 -f 10
```
  
<i>Input files:</i>  
* <i>S. lycopersicum</i> specific <i>k</i>-mers (the output file of <i>identification_of_taxon_specific_kmers.py</i>)  
* ERR418080.fastq, SRR1608100.fastq, SRR2069941.fastq, SRR1481624.fastq (sequencing raw reads downloaded from NCBI SRA database)  
  	
<i>Output files:</i>  
* The filtered list of <i>S. lycopersicum</i> specific <i>k</i>-mers (the count of k-mers and sequences) as binary file  
* The filtered list of <i>S. lycopersicum</i> specific <i>k</i>-mers as human readable TXT file
