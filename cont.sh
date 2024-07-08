#!/bin/bash

output_dir="/home/jvtars/ipe/quantification_results"

gtf_file="/home/jvtars/ipe/GCA_002762385.1_Himp0.1_genomic.gtf"

mkdir -p $output_dir

featureCounts -a $gtf_file -o $output_dir/counts_single.txt /home/jvtars/ipe/bam_files/SRR11144483.sorted.bam

featureCounts -p -a $gtf_file -o $output_dir/counts_paired.txt /home/jvtars/ipe/bam_files/SRR11144484.sorted.bam /home/jvtars/ipe/bam_files/SRR11144485.sorted.bam /home/jvtars/ipe/bam_files/SRR11144486.sorted.bam /home/jvtars/ipe/bam_files/SRR11144481.sorted.bam /home/jvtars/ipe/bam_files/SRR11144482.sorted.bam
