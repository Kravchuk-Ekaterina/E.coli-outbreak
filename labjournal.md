# E.coli outbreak: labjournal

## Exploring the dataset

For this project, we provide three libraries from the TY2482 sample with the following insert sizes and orientation:

###  SRR292678 - paired end, insert size 470 bp (forward reads, reverse reads, 400 Mb each)
1) Forward reads
```bash
wget https://d28rh4a8wq0iu5.cloudfront.net/bioinfo/SRR292678sub_S1_L001_R1_001.fastq.gz
gunzip SRR292678sub_S1_L001_R1_001.fastq.gz
```
2) Reverse reads
```bash    
wget https://d28rh4a8wq0iu5.cloudfront.net/bioinfo/SRR292678sub_S1_L001_R2_001.fastq.gz
gunzip SRR292678sub_S1_L001_R2_001.fastq.gz
```

### SRR292862 – mate pair, insert size 2 kb, (forward reads, reverse reads, 200 Mb each)
1) Forward reads
```bash    
wget https://d28rh4a8wq0iu5.cloudfront.net/bioinfo/SRR292862_S2_L001_R1_001.fastq.gz
gunzip SRR292678sub_S2_L001_R1_001.fastq.gz
``` 
2) Reverse reads
```bash    
wget https://d28rh4a8wq0iu5.cloudfront.net/bioinfo/SRR292862_S2_L001_R2_001.fastq.gz
gunzip SRR292678sub_S2_L001_R2_001.fastq.gz
```

### SRR292770 – mate pair, insert size 6 kb, (forward reads, reverse reads, 200 Mb each)
1) Forward reads
```bash    
wget https://d28rh4a8wq0iu5.cloudfront.net/bioinfo/SRR292770_S1_L001_R1_001.fastq.gz
gunzip SRR292770_S1_L001_R1_001.fastq.gz
``` 
2) Reverse reads
```bash    
wget https://d28rh4a8wq0iu5.cloudfront.net/bioinfo/SRR292770_S1_L001_R2_001.fastq.gz
gunzip SRR292770_S1_L001_R2_001.fastq.gz
```

### FastQC reports

```bash     
fastqc -o . SRR292678sub_S1_L001_R1_001.fastq SRR292678sub_S1_L001_R2_001.fastq SRR292862_S2_L001_R1_001.fastq SRR292862_S2_L001_R2_001.fastq SRR292770_S1_L001_R1_001.fastq SRR292770_S1_L001_R2_001.fastq
```
#### Number of reads:

1) SRR292678 - paired end, insert size 470 bp
Forward reads: 5499346
Reverse reads: 5499346

2) SRR292862 – mate pair, insert size 2 kb
Forward reads: 5102041
Reverse reads: 5102041

3) SRR292770 – mate pair, insert size 6 kb
Forward reads: 5102041
Reverse reads: 5102041

You can find more information in the directory ./fastqc_reports


