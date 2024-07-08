#!/usr/bin/env python3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

file_directory = "/home/jvtars/ipe/quantification_results/"
file_path = os.path.join(file_directory, "combined_counts.txt")

data = pd.read_csv(file_path, sep='\t')

print("Colunas disponíveis no arquivo:", data.columns.tolist())

data.columns = [os.path.basename(col) if col != 'Geneid' else col for col in data.columns]

print("Colunas simples:", data.columns.tolist())

selected_samples = ['SRR11144481.sorted.bam', 'SRR11144482.sorted.bam', 'SRR11144483.sorted.bam']
print("Amostras:", selected_samples)

data_selected = data[['Geneid'] + selected_samples]

selected_scaffolds = ['CDL12_06892', 'CDL12_25384', 'CDL12_00951', 'CDL12_16715', 'CDL12_29787']
data_selected = data_selected[data_selected['Geneid'].isin(selected_scaffolds)]
#Plot
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

for sample in selected_samples:
    sns.lineplot(x='Geneid', y=sample, data=data_selected, label=sample)

plt.title('Rede de Expressão Gênica')
plt.xlabel('Genes')
plt.ylabel('Expressão')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plot_directory = "/home/jvtars/ipe/plots/"
plot_path = os.path.join(plot_directory, "gene_expression_network.png")

plt.savefig(plot_path)
plt.show()

