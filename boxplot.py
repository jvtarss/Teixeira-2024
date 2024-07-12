#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

file_path = "/media/jvtars/807660F07660E7FC/Users/User/Downloads/handro2"
files = ["SRR11144481.csv", "SRR11144482.csv", "SRR11144483.csv", "SRR11144484.csv", "SRR11144485.csv", "SRR11144486.csv"]

genes_of_interest = ["CDL12_25384", "CDL12_21380", "CDL12_29787"]

data = pd.DataFrame()

for file in files:
    df = pd.read_csv(os.path.join(file_path, file))
    df = df[df['Geneid'].isin(genes_of_interest)]
    df = df.set_index('Geneid')
    data = pd.concat([data, df], axis=1)

data.columns = [os.path.splitext(file)[0] for file in files]
data = data.T

data_log2 = np.log2(data + 1)

group_deficit = ["SRR11144481", "SRR11144482", "SRR11144483"]
group_irrigado = ["SRR11144484", "SRR11144485", "SRR11144486"]

data_deficit = data_log2.loc[group_deficit]
data_irrigado = data_log2.loc[group_irrigado]

plt.figure(figsize=(15, 6))

for i, gene in enumerate(genes_of_interest):
    plt.subplot(1, len(genes_of_interest), i + 1)
    data_to_plot = [data_deficit[gene], data_irrigado[gene]]
    plt.boxplot(data_to_plot, labels=['Déficit', 'Irrigado'])
    plt.title(f'Gene: {gene}')
    plt.ylim(0, data_log2.max().max() + 1)
    plt.ylabel('Expression Levels (log2)' if i == 0 else '')

plt.suptitle('Boxplot of Gene Expression Levels (log2 normalized)')
plt.tight_layout(rect=[0, 0, 1, 0.95])

output_path = "/media/jvtars/807660F07660E7FC/Users/User/Downloads/handro2/boxplot_log2_comparison.png"
plt.savefig(output_path)
plt.show()
