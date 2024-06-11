#!/usr/bin/env python3

import pandas as pd

# carregamento de arquivos de contagem e filtragem de colunas
counts_single = pd.read_csv("/home/jvtars/ipe/quantification_results/counts_single.txt", sep='\t', comment='#', index_col=0)
counts_paired = pd.read_csv("/home/jvtars/ipe/quantification_results/counts_paired.txt", sep='\t', comment='#', index_col=0)
counts_single = counts_single.iloc[:, 5:]
counts_paired = counts_paired.iloc[:, 5:]

# combinação
combined_counts = pd.concat([counts_single, counts_paired], axis=1)
combined_counts.to_csv("/home/jvtars/ipe/quantification_results/combined_counts.txt", sep='\t')
