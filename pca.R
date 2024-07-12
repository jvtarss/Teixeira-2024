library(ggplot2)
library(dplyr)

files <- list.files(path = "C:/Users/User/Downloads/handro2", pattern = "SRR1114448[1-6].csv", full.names = TRUE)
data_list <- lapply(files, read.csv)
names(data_list) <- c("SRR11144481", "SRR11144482", "SRR11144483", "SRR11144484", "SRR11144485", "SRR11144486")

combined_data <- Reduce(function(x, y) merge(x, y, by = "Geneid"), data_list)
rownames(combined_data) <- combined_data$Geneid
combined_data <- combined_data[,-1]

log2_data <- log2(combined_data + 1)

log2_data <- log2_data[rowSums(log2_data) != 0, ]
log2_data <- log2_data[, apply(log2_data, 2, var) != 0]

pca <- prcomp(t(log2_data), scale. = TRUE)
pca_data <- as.data.frame(pca$x)
pca_data$Sample <- rownames(pca_data)
pca_data$Group <- ifelse(pca_data$Sample %in% c("SRR11144481", "SRR11144482", "SRR11144483"), "Déficit", "Irrigado")

ggplot(pca_data, aes(x = PC1, y = PC2, color = Group)) +
  geom_point(size = 4) +
  labs(title = "PCA de Similaridade entre Amostras", x = "PC1", y = "PC2") +
  theme_minimal()
