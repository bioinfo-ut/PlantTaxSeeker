# IDENTIFICATION OF PLANT TAXON SPECIFIC K-MERS AND COUNTING K-MERS FROM METAGENOMIC WGS READS 
Scripts for identification taxon-specific <i>k</i>-mers from plant genomes and for the detection and counting the k-mers directly from WGS reads of metagenomic sample.  
  
PlantTaxSeeker scripts are licensed under the GPLv3 license.  
  
The scripts consists predominantly of code written in Python (tested in UNIX server with Python versions 2.7 and 3.3) and also use:  
`glistmaker`, `glistcompare`, `glistquery`, `MakeUnion.pl` and `gmer_counter` from the [GenomeTester4 package](https://github.com/bioinfo-ut/GenomeTester4/)

## Usage
### 1. To identify target taxon specific <i>k</i>-mers, use command:  

```
python identification_of_taxon_specific_kmers.py <Targets.fasta> <Nontargets.fasta> [optional_arguments]
```

The optional arguments can also be specified:  
* -w Length of the <i>k</i>-mer (default value 32)  
* -f The minimum number of target sequences that should contain every specific <i>k</i>-mers (default value 1)  

<i>Input files:</i>  
* Target taxon genome sequences as FASTA format file  
* Nontarget taxa genome sequences as FASTA format file  

<i>Output files:</i>   
* The list of target taxon specific <i>k</i>-mers (the count of <i>k</i>-mers and sequences) as binary file  
* The list of target taxon specific <i>k</i>-mers (the count of <i>k</i>-mers and sequences) as TEXT file  

### 2. To filter out additional non-specific <i>k</i>-mers using whole genome sequencing raw reads or assembled sequences of nontarget taxa, use command.  

```
python filtering_with_nontargets.py <Specific_kmers.list> <Nontarget1.fastq> [Nontargets fastqs] [optional_arguments]
```

The optional arguments can also be specified:  
* -w	Length of the <i>k</i>-mer (bases, by default 32)  
* -f	The <i>k</i>-mer frequency cutoff (only <i>k</i>-mers from nontarget sequences with at least given frequency cutoff will be filtered out from target <i>k</i>-mer list) (by default 10)  
  
<i>Input files:</i>
* Unfiltered target taxon specific <i>k</i>-mers list as binary file (the output file of <i>identification_of_taxon_specific_kmers.py</i>)  
* Nontarget taxon fastq files for filtering nonspecific <i>k</i>-mers  

<i>Output files:</i>
* Target taxon specific <i>k</i>-mers list as binary file (contains only <i>k</i>-mers that are not in nontarget taxa fastq files)  
* Target taxon specific <i>k</i>-mers list as TXT file  

### An example: the identification of <i>Solanum lycopersicum</i> specific <i>k</i>-mers:  
README file for executing scripts for the identification <i>Solanum lycopersicum</i> specific <i>k</i>-mers are available in [Github](https://github.com/bioinfo-ut/PlantTaxSeeker/blob/master/example/README.md)

### 3. To detect and count plant taxa specific <i>k</i>-mers from whole genome sequencing raw reads of metagenomic sample, use command.  

```
python plant_taxa_kmers_counter.py <Specific_kmers.list> <Metagenomic_sample.fastq> [optional_argument]
```

The optional argument can also be specified:    
* -f	The <i>k</i>-mer frequency cutoff (only <i>k</i>-mers with at least given frequency cutoff will be counted from metagenomic sequencing reads) (by default 1)  
  
<i>Input files:</i>
* Target taxon specific <i>k</i>-mers list as TXT file (the output file of <i>identification_of_taxon_specific_kmers.py</i>)  
* fastq file of WGS reads from metagenomic sample  

<i>Output</i>
*  The count of detected target plant taxon specific <i>k</i>-mers in WGS reads from metagenomic sample.
### An example: the identification of <i>Lupinus spp.</i> specific <i>k</i>-mers and counting <i>Lupinus spp.</i> specific <i>k</i>-mers from WGS reads of lupin-containing cookie:  
README file for executing scripts for the identification <i>Lupinus spp.</i> specific <i>k</i>-mers and for counting of <i>Lupinus spp.</i> specific <i>k</i>-mers from cookie WGS data are available in [Github](https://github.com/bioinfo-ut/PlantTaxSeeker/blob/master/example2/README.md)
