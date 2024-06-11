#!/usr/bin/env Rscript

# Carregar as bibliotecas necessárias
library(DESeq2)
library(ggplot2)
library(pheatmap)

# Ler os dados de contagem
countData <- read.table("/home/jvtars/ipe/quantification_results/combined_counts.txt", header=TRUE, row.names=1)

# Preparar as informações das amostras
sampleInfo <- data.frame(
  row.names = colnames(countData),
  condition = c("condition1", "condition1", "condition1", "condition2", "condition2", "condition2")
)

# Criar o dataset DESeq2
dds <- DESeqDataSetFromMatrix(countData = countData, colData = sampleInfo, design = ~ condition)

# Executar a análise de expressão diferencial
dds <- DESeq(dds)

# Obter os resultados
res <- results(dds)

# Salvar os resultados em um arquivo
write.csv(as.data.frame(res), file="/home/jvtars/ipe/differential_expression_results.csv")

# Gráfico MA
png("/home/jvtars/ipe/plots/MA_plot.png")
plotMA(res, main="MA Plot", ylim=c(-2,2))
dev.off()

# Gráfico de vulcão
res$log2FoldChange <- as.numeric(res$log2FoldChange)
res$pvalue <- as.numeric(res$pvalue)
res$padj <- as.numeric(res$padj)
res$significant <- ifelse(res$padj < 0.05, "Significant", "Not Significant")

png("/home/jvtars/ipe/plots/Volcano_plot.png")
ggplot(res, aes(x=log2FoldChange, y=-log10(pvalue), color=significant)) +
  geom_point(alpha=0.4, size=1.75) +
  theme_minimal() +
  scale_color_manual(values=c("red", "black")) +
  labs(title="Volcano Plot", x="Log2 Fold Change", y="-Log10 P-value")
dev.off()

# Heatmap dos 20 genes mais diferencialmente expressos
top20 <- head(order(res$padj), 20)
mat <- assay(rlog(dds))[top20,]
mat <- mat - rowMeans(mat)
png("/home/jvtars/ipe/plots/Heatmap.png")
pheatmap(mat, cluster_rows=TRUE, show_rownames=TRUE, cluster_cols=TRUE)
dev.off()
