data(InsectSprays)
barplot(tapply(InsectSprays$count, InsectSprays$spray, mean),
        xlab = "Spray Type", ylab = "Average Insect Count",
        main = "Effectiveness of Insect Sprays", col = "skyblue")


# Load dataset
data(PlantGrowth)

# Compute mean values

# Convert to % of total if you want a "percent of cells" style
percent <- round(100 * means / sum(means), 1)

# Create matrix for grouped barplot (you can duplicate or simulate more groups)
d.val <- rbind(percent, percent + 10, percent + 5)  

# Fake additional drugs for demo

# Create bar plot
barplot(
  d.val,
  beside = TRUE,
  ylim = c(0, 100),
  ylab = "% of cells",
  col = c("gray70", "skyblue", "salmon"),
  legend.text = c("Untreated", "Drug A", "Drug B"),
  args.legend = list(bty = "n", x = "topright")
)

