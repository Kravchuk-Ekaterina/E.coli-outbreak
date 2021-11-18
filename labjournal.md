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

-m or “mer” specifies the length <br>
-C tells it to ignore directionality (it treats each read the same as its reverse complement).<br>
-s is an initial estimate for the size of the hash table jellyfish uses, set > genome size<br>
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

## 3. Assembling E. coli X genome from paired reads

We will use assembler SPAdes.

### 3.1. Dowloading and unpacking SPAdes

```bash
wget https://cab.spbu.ru/files/release3.15.2/SPAdes-3.15.2-Linux.tar.gz
gunzip SPAdes-3.15.2-Linux.tar.gz
tar -xvf SPAdes-3.15.2-Linux.tar
```

Testing:
```bash
spades.py --test
```
### 3.2. Assembling genome from the library SRR292678

```bash
spades.py --pe1-1 SRR292678sub_S1_L001_R1_001.fastq --pe1-2 SRR292678sub_S1_L001_R2_001.fastq -o SRR292678
```

### 3.3. Quality of the resulting assembly

We use QUAST online tool on scaffolds.fasta and contigs.fasta

#### report for contigs.fasta:
![contigs report](./images/contigs_report.jpg "contigs report")

#### report for scaffolds.fasta:
![scaffolds report](./images/scaffolds_report.jpg "scaffolds report")

### 3.4. Effect of read correction

Using jellyfish on corrected files:

```bash
jellyfish count -m 31 -C -s 5499346 -o kmercorrected SRR292678/corrected/SRR292678sub_S1_L001_R1_001.00.0_0.cor.fastq
```

Creating the histogram file

```bash
jellyfish histo kmercorrected > kmercorrectedhist.txt
```

#### Then I made the plot using ./scripts/k-mer.py
![corrected k-mer distribution](./scripts/kmer_corrected.png "corrected k-mer distribution")

There are fewer low frequent reads in corrected reads, which are related to sequencing errors.

## 4. Impact of reads with large insert size

### 4.1. Running SPAdes
Now we run SPAdes by consolidating three libraries. We use all three libraries: SRR292678 as a paired ends, SRR292862 and SRR292770 as a mate pairs.

```bash
spades.py --pe1-1 SRR292678sub_S1_L001_R1_001.fastq --pe1-2 SRR292678sub_S1_L001_R2_001.fastq --mp1-1 SRR292862_S2_L001_R1_001.fastq --mp1-2 SRR292862_S2_L001_R2_001.fastq --mp2-1 SRR292770_S1_L001_R1_001.fastq --mp2-2 SRR292770_S1_L001_R2_001.fastq -o assembly2
```
We use QUAST online tool on scaffolds.fasta and contigs.fasta

#### report for contigs.fasta:
![contigs report](./images/contigs_report2.jpg "contigs report")

#### report for scaffolds.fasta:
![scaffolds report](./images/scaffolds_report2.jpg "scaffolds report")

N50 becomes higher, it happened through the use of mate pairs, which increases assembly accuracy solving repeats.


