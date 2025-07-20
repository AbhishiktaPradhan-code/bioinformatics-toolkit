# Load ggplot2 and ggrepel
library(ggplot2)
library(ggrepel)

# Simulate volcano data
set.seed(123)
v.data <- data.frame(
  gene_symbol = paste0("Gene", 1:1000),
  log2FoldChange = rnorm(1000, mean = 0, sd = 2),
  pvalue = runif(1000, min = 0, max = 1)
)

# Add differential expression status
v.data$diffexpressed <- "NO"
v.data$diffexpressed[v.data$log2FoldChange >= 1 & v.data$pvalue <= 0.05] <- "UP"
v.data$diffexpressed[v.data$log2FoldChange <= -1 & v.data$pvalue <= 0.05] <- "DOWN"

# Create a new label column: only label UP or DOWN genes
v.data$glabel <- NA
v.data$glabel[v.data$diffexpressed != "NO"] <- v.data$gene_symbol[v.data$diffexpressed != "NO"]

# Plot
ggplot(data = v.data, aes(x = log2FoldChange, y = -log10(pvalue), col = diffexpressed, label = glabel)) +
  geom_point(alpha = 0.7) +
  scale_color_manual(values = c("DOWN" = "blue", "NO" = "grey", "UP" = "red")) +
  geom_vline(xintercept = c(-1, 1), col = "black", linetype = "dashed") +
  geom_hline(yintercept = -log10(0.05), col = "black", linetype = "dashed") +
  geom_text_repel(na.rm = TRUE, max.overlaps = 15, size = 3) +
  theme_minimal() +
  labs(title = "Volcano Plot with Gene Labels",
       x = "log2 Fold Change",
       y = "-log10(p-value)",
       color = "Expression")
