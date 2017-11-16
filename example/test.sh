#!/bin/bash

cp ../bin/* .
cp ../scripts/* .

chmod 755 glistquery
chmod 755 glistmaker
chmod 755 glistcompare
chmod 755 MakeUnion.pl

# Download  FASTQ and FASTA files
wget http://www.bioinfo.ut.ee/PlantTaxSeeker/ERR418080.fastq.gz
wget http://www.bioinfo.ut.ee/PlantTaxSeeker/Nontarget_taxa_complete_chl_genomes_07Jan16.fasta.gz
wget http://www.bioinfo.ut.ee/PlantTaxSeeker/SRR1481624.fastq.gz
wget http://www.bioinfo.ut.ee/PlantTaxSeeker/SRR1608100.fastq.gz
wget http://www.bioinfo.ut.ee/PlantTaxSeeker/SRR2069941.fastq.gz
wget http://www.bioinfo.ut.ee/PlantTaxSeeker/Solanum_lycopersicum_complete_chl_genomes_07Jan16.fasta.gz
gunzip *gz

# Identify k-mers that are specific to Solanum lycopersicum
python identification_of_taxon_specific_kmers.py Solanum_lycopersicum_complete_chl_genomes_07Jan16.fasta Nontarget_taxa_complete_chl_genomes_07Jan16.fasta -f 2

# Run additional filtering with raw reads of non-target genomes
python filtering_with_nontargets.py Specific_kmers_32.list ERR418080.fastq SRR1608100.fastq SRR2069941.fastq SRR1481624.fastq -f 10
