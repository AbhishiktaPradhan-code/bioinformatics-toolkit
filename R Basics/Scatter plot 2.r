# Simulated ELISA data: 10 concentrations, each with 3 replicate absorbance readings
set.seed(42)
elisa_data <- data.frame(
  conc = seq(0.1, 1.0, by = 0.1),
  rep1 = runif(10, 0.2, 1.0),
  rep2 = runif(10, 0.2, 1.0),
  rep3 = runif(10, 0.2, 1.0)
)

# View data
head(elisa_data)

# Calculate mean of columns 2 to 4 (rep1 to rep3)
abs_mean <- rowMeans(elisa_data[, 2:4])

# Add it to the data frame (optional)
elisa_data$mean_abs <- abs_mean

plot(
  elisa_data$conc,                   # x-axis: concentration
  elisa_data$mean_abs,              # y-axis: mean absorbance
  xlab = "Concentration (ng/ml)",   # x-axis label
  ylab = "Absorbance",              # y-axis label
  pch = 19,                         # solid circle point
  col = "blue",                     # point color
  cex = 2,                          # point size
  xlim = c(0, 1.4),                 # x-axis range
  ylim = c(0, 2),                   # y-axis range
  main = "ELISA Standard Curve"     # optional: title
)


plot(
  elisa_data$conc,
  elisa_data$mean_abs,
  xlab = "Concentration (ng/ml)",
  ylab = "Absorbance",
  pch = 19,
  col = "blue",
  cex = 2,
  xlim = c(0, 1.4),
  ylim = c(0, 2),
  type = "b",          # BOTH points and lines
  lwd = 2,             # line width
  main = "ELISA Standard Curve"
)
 data()
 