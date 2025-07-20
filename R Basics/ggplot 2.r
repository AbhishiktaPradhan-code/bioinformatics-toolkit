
# Use of statistics layer in ggplot2

# This script uses ggplot2 package.
# Install it before the use.
# Load the package
library (ggplot2)

# Example 1: calling statistics within a geom
# Generate mock FACS data
set.seed(123)
facs <- data.frame(
  FSC.H = rnorm(1000, mean = 50000, sd = 8000),
  SSC.H = rnorm(1000, mean = 20000, sd = 5000),
  FL1.H = rnorm(1000, mean = 100, sd = 30),
  FL2.H = rnorm(1000, mean = 150, sd = 40)
)

# Save to CSV
write.csv(facs, "flow.csv", row.names = FALSE)

facs.plotl <- ggplot (facs,
                      aes (x = FL2.H)) +geom_histogram()

facs.plotl 

# Use smaller bin width
facs.plot2 <- ggplot(facs,
                     aes (x = FL2.H)) +
  geom_histogram(binwidth = 5)
facs.plot2


# Final histogram

facs.plot3 <-ggplot(facs, aes(x = FL2.H)) +
  geom_histogram(binwidth = 5, fill = "skyblue", color = "black") +
  labs(x = "FL2-H", y = "Count") +
  ylim(0, 75) +
  theme_classic()+
  theme(
    axis.text = element_text(size = 12, family = "sans"),
    axis.title = element_text(size = 12, family = "sans")
  )
facs.plot3


# Example 2: calling statistics within a geom b

# Read the InsectSprays data of R
# and create a box plot to show effects of
# different insecticides
# Load data
d <- InsectSprays
# Create Box plot using geom_boxplot
box_plot <- ggplot(InsectSprays, aes(x = spray, y = count, color = spray)) +
  geom_boxplot(
    outlier.colour = "red",
    outlier.shape = 16,
    outlier.size = 3,
    show.legend = FALSE
  ) +
  labs(x = "Type of spray", y = "Insect Count") +
  ylim(0, 30) +
  theme_classic() +
  theme(
    axis.text = element_text(size = 12, family = "sans"),
    axis.title = element_text(size = 14, family = "sans")
  )
box_plot

# Example 3: calling statistics independently

# Read data
bar.data <- iris

# Create the bar plot showing mean values

# Use stat_summary to getIstatistics,
# like mean and sd.error

library(ggplot2)

bar.plot1 <- ggplot(bar.data,
                    aes(x = Species, y = Petal.Length)) +
  stat_summary(fun.data = mean_se,
               geom = "bar",
               fill = "skyblue") +
  labs(x = "Species", y = "Mean Petal Length") +
  theme_minimal()

bar.plot1

# Add error bars (standard deviation limit)
bar.plot2 <- bar.plot1 +
  stat_summary(fun.data = mean_sdl,
               fun.args = list(mult = 1),
               geom = "errorbar",
               width = 0.5)

bar.plot2



library(ggplot2)

bar.plot3 <- ggplot(bar.data, 
                    aes(x = Species, y = Petal.Length)) +
  stat_summary(fun.data = mean_sdl,
               fun.args = list(mult = 1),
               geom = "errorbar",
               width = 0.5) +
  stat_summary(fun.data = mean_se,
               geom = "bar",
               fill = "skyblue") +
  labs(x = "Species", y = "Petal Length") +
  theme_minimal()

bar.plot3
  
#final bar plot

bar.plot4 <-ggplot(bar.data,
       aes(x = Species, y = Petal.Length)) +
  stat_summary(fun.data = mean_sdl,
               fun.args = list(mult = 1),
               geom = "errorbar",
               width = 0.5) +
  stat_summary(fun.data = mean_se,
               geom = "bar",
               fill = "skyblue") +
  labs(
    x = "Species",
    y = "Petal Length"
  ) +
  ylim(0, 8) +
  theme_classic() +
  theme(
    axis.text = element_text(size = 14, family = "sans"),
    axis.title = element_text(size = 14, family = "sans")
  )

bar.plot4 
