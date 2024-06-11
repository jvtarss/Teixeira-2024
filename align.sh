#!/bin/bash

# Define the sample and reference genome
sample="SRR11144483"
reference_genome="/home/jvtars/ipe/GCA_002762385.1_Himp0.1_genomic"
fastq_file="/home/jvtars/ipe/sra_data/${sample}.fastq.gz"
output_dir="/home/jvtars/ipe/alignment_results"

# Create the output directory if it doesn't exist
mkdir -p $output_dir

# Align the reads using HISAT2
hisat2 -x $reference_genome -U $fastq_file -S ${output_dir}/${sample}.sam
