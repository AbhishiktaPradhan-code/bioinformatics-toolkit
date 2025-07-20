# Scatter plot

# Data used: Default dataset 'DNase' of R
# The data
d <- DNase
# Our first scatter plot
plot(d$conc, d$density)
# Formatting the plot
# xlab, ylab for axes labels
# pch for symbol or shape of points
# col for color of symbol
# cex size of symbol
# cex.axis and cex. label for font sizes

plot (d$conc,
      d$density,
      xlab = "Concentration (ng/ml)",
      ylab = "Absorbance",
      pch = 3,
      col = "blue",
      cex = 2,
      cex.axis = 1.5,
      cex.lab = 1.5)

# Plot the mean of multiple runs
# Calculate the mean absorbance for
# each concentration using aggregate()

d.avg <- aggregate(density ~ conc, d, mean)


# Plot conc vs mean absorbance

plot(d.avg$conc, d.avg$density,
     xlab = "Concentration (ng/ml)",
     ylab = "Absorbance",
     pch = 19,
     col = "blue",
     cex = 2,
     cex.axis = 1.5,
     cex.lab = 1.5)

# Edit axes limits
# Set xlim and ylim arguments
plot(d.avg$conc, d.avg$density,
     xlab = "Concentration (ng/ml)",
     ylab = "Absorbance",
     pch = 19,
     col = "blue",
     cex = 2,
     cex.axis = 1.5,
     cex.lab = 1.5,
     xlim = c(0, 14),
     ylim = c(0,2))
