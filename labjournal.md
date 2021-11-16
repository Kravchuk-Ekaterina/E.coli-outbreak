# E.coli outbreak: labjournal

## 1. Exploring the dataset

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

## 2. K-mer profile and genome size estimation
To count kmers, we will use the Jellyfish

### 2.1. Installing Jellyfish

```bash     
sudo apt-get install jellyfish
```

### 2.2. Counting k-mers

The “jellyfish count” command takes the following options:

-m or “mer” specifies the length
-C tells it to ignore directionality (it treats each read the same as its reverse complement).
-s is an initial estimate for the size of the hash table jellyfish uses, set > genome size
-o specifies the name of the output file. choose a name with the k-mer length in it.

1) Running "jellyfish count" command
```bash
jellyfish count -m 31 -C -s 5499346 -o kmer SRR292678sub_S1_L001_R1_001.fastq
```

2) Creating the histogram file
```bash
jellyfish histo kmer > kmerhist.txt
```

### 2.3. Visualizing k-mer distribution
I created the script ./scripts/k-mer.py to visualize k-mer distribution

#### k-mer distribution
![k-mer distribution](./scripts/kmer_dist.png "k-mer distribution")

#### The border of the initial peak corresponding to sequence errors at 5
![err-5](./scripts/err_5.png "err-5")

### 2.4. 2.4. Estimate the genome size
To estimate the genome size I modified k-mer.py
The answer is 5199855

