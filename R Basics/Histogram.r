# Load the 'faithful' dataset (Old Faithful geyser eruptions)
data(faithful)

# 1. Basic histogram
hist(faithful$eruptions,
     main = "Basic Histogram of Eruption Durations",
     xlab = "Duration (min)",
     col = "lightgray")

# 2. Histogram with mean and median lines
hist(faithful$eruptions,
     breaks = 20,                    # Number of bins
     probability = TRUE,            # Show density, not counts
     col = "lightblue",
     main = "Eruption Duration Distribution",
     xlab = "Duration (min)")
abline(v = mean(faithful$eruptions), col = "red", lwd = 2, lty = 2)      # Mean line
abline(v = median(faithful$eruptions), col = "darkgreen", lwd = 2, lty = 3)  # Median line
legend("topright", legend = c("Mean", "Median"),
       col = c("red", "darkgreen"), lty = c(2, 3), bty = "n")

# 3. Histogram using Freedman–Diaconis rule
hist(faithful$eruptions,
     breaks = "FD",                     # Freedman–Diaconis bin width
     col = "skyblue",
     border = "white",
     xlim = c(1, 6),
     ylim = c(0, 0.6),
     xlab = "Eruption Duration (minutes)",
     ylab = "Density",
     main = "Old Faithful Eruptions (FD Rule)",
     las = 1,
     probability = TRUE)

# 4. Histogram showing density with 40 bins
hist(faithful$eruptions,
     breaks = 40,
     freq = FALSE,                    # Show density
     xlim = c(1, 6),
     col = "lightblue",
     border = "white",
     xlab = "Eruption Duration (min)",
     main = "Eruption Histogram (Density)",
     las = 1)

# 5. Histogram with percentage on y-axis
# Step 1: Create histogram object without plotting
h <- hist(faithful$eruptions, plot = FALSE)

# Step 2: Convert counts to percentages
h$density <- h$counts * 100 / sum(h$counts)

# Step 3: Plot histogram with percentage y-axis
plot(h,
     freq = FALSE,                     # Use h$density values
     col = "lightblue",
     border = "white",
     xlab = "Eruption Duration (min)",
     ylab = "Percentage of Observations",
     main = "Eruption Histogram (% Scale)",
     las = 1,
     ylim = c(0, max(h$density) + 2))  # Extra space above tallest bar

