#!/usr/bin/env Rscript

lib_path <- "~/R/x86_64-pc-linux-gnu-library/4.0"

if (!dir.exists(lib_path)) {
  dir.create(lib_path, recursive = TRUE)
}

.libPaths(lib_path)

install.packages("BiocManager", lib = lib_path)
BiocManager::install("DESeq2", lib = lib_path)
install.packages("ggplot2", lib = lib_path)
install.packages("pheatmap", lib = lib_path)
