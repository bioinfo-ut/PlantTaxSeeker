# IDENTIFICATION OF PLANT TAXON SPECIFIC K-MERS  
Scripts for identification taxon-specific <i>k</i>-mers from plant genomes.  

The scripts consists predominantly of code written in Python (tested in UNIX server with Python versions 2.7 and 3.3) and also use:  
`glistmaker`, `glistcompare`, `glistquery` and `MakeUnion.pl` from the [GenomeTester4 package](https://github.com/bioinfo-ut/GenomeTester4/)

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
* Unfiltered target taxon specific <i>k</i>-mers list as binary file (the output file of <i>Pipeline_for_identification_taxon_specific_kmers_ver1.py</i>)  
* Nontarget taxon fastq files for filtering nonspecific <i>k</i>-mers  

<i>Output files:</i>
* Target taxon specific <i>k</i>-mers list as binary file (contains only <i>k</i>-mers that are not in nontarget taxa fastq files)  
* Target taxon specific <i>k</i>-mers list as TXT file  

### 3. An example: the identification of <i>Solanum lycopersicum</i> specific <i>k</i>-mers (see [README1 file in Github](https://github.com/bioinfo-ut/PlantTaxSeeker/example_files/)):  
* Chloroplast complete genome sequences for <i>Solanum lycopersicum</i> as the target taxon and for nontarget taxa are available from [Github](https://github.com/bioinfo-ut/PlantTaxSeeker/example_files/)  
* README file for executing scripts for the identification <i>Solanum lycopersicum</i> specific <i>k</i>-mers are available from [Github](https://github.com/bioinfo-ut/PlantTaxSeeker/example_files/)
