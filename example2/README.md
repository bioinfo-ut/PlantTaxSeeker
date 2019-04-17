# AN EXAMPLE OF DETECTION AND COUNTING <i>LUPINUS SPP.</i> SPECIFIC <i>K</i>-MERS DIRECTLY FROM  WGS READS FROM LUPIN-CONTAINING COOKIE 
In this example we are detecting and counting <i>Lupinus spp.</i> specific <i>k</i>-mers with length 32 bases present in WGS reads from COOKIE containing 5% lupin flour in wheat flour.
  
Before you can start, you need to:
* a) identify <i>Lupinus spp.</i> specific <i>k</i>-mers with length 32 bases, using the pipeline described for the identification of plant taxa specific <i>k</i>-mers [HERE](https://github.com/bioinfo-ut/PlantTaxSeeker), example for <i>S. lycopersicum</i> is [HERE](https://github.com/bioinfo-ut/PlantTaxSeeker/blob/master/example/README.md), or use our example file of <i>Lupinus spp.</i> specific <i>k</i>-mers).
* b) download PlantTaxSeeker repository containing bins, scripts and readme files from [Github](https://github.com/bioinfo-ut/PlantTaxSeeker) 
* c) move to the folder "example2"
* d) download sequencing data of cookie sample as FASTQ-format file and the list of <i>Lupinus spp.</i> specific <i>k</i>-mers with length 32 bases [HERE](http://www.bioinfo.ut.ee/PlantTaxSeeker/).    
    
Make sure you have enough space for storing these files. The size of FASTQ file of cookie WGS is about 5.3 Gb.

Use following command lines to perform the example analysis ("bash test.sh" downloads FASTA and FASTQ files, moves bins and scripts needed for analysis to the folder "example2" and executes scripts):
```  
git clone https://github.com/bioinfo-ut/PlantTaxSeeker/
cd PlantTaxSeeker/example2/
bash test.sh
```  
   
As a result you get the number of detected <i>Lupinus spp.</i> specific <i>k</i>-mers that were present in WGS reads from cookie.  
