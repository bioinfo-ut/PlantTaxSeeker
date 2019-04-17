#!bin/bash
#Script for testing the detection and counting Lupinus spp. specific k-mers

cp ../bin/* .
cp ../scripts/* .

chmod 755 gmer_counter
chmod 755 plant_taxa_kmers_counter.py

# Download FASTQ and TXT files
echo Downloading files ...
wget http://www.bioinfo.ut.ee/PlantTaxSeeker/Lupinus_spp_specific_kmers_w32_31179.txt
wget http://www.bioinfo.ut.ee/PlantTaxSeeker/21BCookie.fastq

# Counting Lupinus spp. specific k-mers from cookie FASTQ
echo Detecting and counting of Lupinus spp. specific k-mers from FASTQ file ...
python plant_taxa_kmers_counter.py Lupinus_spp_specific_kmers_w32_31179.txt 21BCookie.fastq -f 1

echo Finished!
