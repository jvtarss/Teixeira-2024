#!/bin/bash

# Diretório de saída para os resultados de quantificação
output_dir="/home/jvtars/ipe/quantification_results"

# Arquivo GTF de anotação
gtf_file="/home/jvtars/ipe/GCA_002762385.1_Himp0.1_genomic.gtf"

# Criar diretório de saída se não existir
mkdir -p $output_dir

# Quantificação para SRR11144483 (single-end)
featureCounts -a $gtf_file -o $output_dir/counts_single.txt /home/jvtars/ipe/bam_files/SRR11144483.sorted.bam

# Quantificação para SRR11144484, SRR11144485, SRR11144486, SRR11144481, SRR11144482 (paired-end)
featureCounts -p -a $gtf_file -o $output_dir/counts_paired.txt /home/jvtars/ipe/bam_files/SRR11144484.sorted.bam /home/jvtars/ipe/bam_files/SRR11144485.sorted.bam /home/jvtars/ipe/bam_files/SRR11144486.sorted.bam /home/jvtars/ipe/bam_files/SRR11144481.sorted.bam /home/jvtars/ipe/bam_files/SRR11144482.sorted.bam
