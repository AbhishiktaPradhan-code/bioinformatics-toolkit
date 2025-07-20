
# Load the dataset
data("ToothGrowth")

# Store into a new variable (optional)
ToothGrowth.data <- ToothGrowth

# Summary statistics
summary(ToothGrowth.data)

# Print the full data (optional)
print(ToothGrowth.data)

# Boxplot: Tooth length by Supplement type
boxplot(
  len ~ supp,
  data = ToothGrowth.data,
  main = "Tooth Length by Supplement Type",
  xlab = "Supplement",
  ylab = "Tooth Length",
  col = c("lightblue", "lightgreen")
)

#Shapiro-Wilk test for TJ group
#Before doing parametric tests like t-test or ANOVA
# Null hypthesis: Data is Normally distributed
#To check the assumption that each group’s residuals are normally distributedShapiro-Wilk test for VC group
shapiro.test(ToothGrowth.data$len[ToothGrowth.data$supp == "VC"])

# Shapiro-Wilk test for OJ group
shapiro.test(ToothGrowth.data$len[ToothGrowth.data$supp == "OJ"])


# F test to check equal variance.
# Null hypothesis: Variances of two samples are equal

# Subset the two groups
VC_len <- ToothGrowth$len[ToothGrowth$supp == "VC"]
OJ_len <- ToothGrowth$len[ToothGrowth$supp == "OJ"]

# Variance test (F-test)
var.test(VC_len, OJ_len)

# Perform unpaired (independent) t-test assuming equal variances
t.test(OJ_len, VC_len, var.equal = TRUE)

# Perform one-way ANOVA 
#H₀: All group means are equal
#H₁: At least one group mean is different
#If p < 0.05 → significant difference among group means
oneway.test(len ~ supp, data = ToothGrowth, var.equal = TRUE)


