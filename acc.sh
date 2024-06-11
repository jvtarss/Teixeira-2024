#!/bin/bash

# List of SRA accessions
sra_accessions=(
    "SRR11144484"
    "SRR11144485"
    "SRR11144486"
)

download_dir="/home/jvtars/ipe/sra_data"

mkdir -p $download_dir

for accession in "${sra_accessions[@]}"; do
    fastq-dump --outdir $download_dir --gzip --skip-technical --readids --read-filter pass --dumpbase --split-files --clip $accession
done
