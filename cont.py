#!/usr/bin/env python3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

file_directory = "/home/jvtars/ipe/quantification_results/"
file_path = os.path.join(file_directory, "combined_counts.txt")

# Ler o arquivo com o delimitador correto
data = pd.read_csv(file_path, sep='\t')

# Verificar os nomes das colunas
print("Colunas disponíveis no arquivo:", data.columns.tolist())

# Remover os caminhos dos nomes das colunas
data.columns = [os.path.basename(col) if col != 'Geneid' else col for col in data.columns]

# Verificar os nomes das colunas novamente após a simplificação
print("Colunas simplificadas:", data.columns.tolist())

selected_samples = ['SRR11144481.sorted.bam', 'SRR11144482.sorted.bam', 'SRR11144483.sorted.bam']
print("Amostras selecionadas:", selected_samples)

# Selecionar apenas as colunas de interesse
data_selected = data[['Geneid'] + selected_samples]

# Filtrar os genes de interesse
selected_scaffolds = ['CDL12_06892', 'CDL12_25384', 'CDL12_00951', 'CDL12_16715', 'CDL12_29787']
data_selected = data_selected[data_selected['Geneid'].isin(selected_scaffolds)]

# Plotar os dados
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

