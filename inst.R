#!/usr/bin/env Rscript

# Definir um diretório de biblioteca específico no diretório home
lib_path <- "~/R/x86_64-pc-linux-gnu-library/4.0"

# Criar o diretório de biblioteca se ele não existir
if (!dir.exists(lib_path)) {
  dir.create(lib_path, recursive = TRUE)
}

# Definir o diretório de biblioteca
.libPaths(lib_path)

# Instalar pacotes no diretório de biblioteca especificado
install.packages("BiocManager", lib = lib_path)
BiocManager::install("DESeq2", lib = lib_path)
install.packages("ggplot2", lib = lib_path)
install.packages("pheatmap", lib = lib_path)
