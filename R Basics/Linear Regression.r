# **** Linear Regression ****

# Data used: Helmut Spaeth, Mathematical Algorithms for Linear
# Regression (1991)and D G Kleinbaum and L L Kupper,
# Applied Regression Analysis and Other Multivariable Methods (1978)

# In simple liner regression you create linear model
# y = a + bx I
# x is the independent variable or predictor.
 # y is dependent variable or response.

# Use the linear model function lm()
# Read data ----
# Load the dataset
data(mtcars)

# Fit the linear model (mpg predicted by wt)
model <- lm(mpg ~ wt, data = mtcars)

# Scatter plot
plot(mtcars$wt, mtcars$mpg,
     xlab = "Weight (wt)",
     ylab = "Miles per Gallon (mpg)",
     pch = 19,
     col = "blue",
     main = "Linear Regression: MPG vs Weight")

# Add regression line
abline(model, col = "red", lwd = 2)

# Calculate the Pearson's Correlation 
# Use cor() function

cor(mtcars$mpg, mtcars$wt, method = "pearson")

# Perform linear rearession usina lm function
# Predictor/Independent - wt
# Response/dependent - mpg
# Fit the linear model (mpg predicted by wt)
model <- lm(mpg ~ wt, data = mtcars)

# Get the summary of regression ----
# (1) Value of the coefficients
# (2) R-squared value
# (2) t-test result

summary(model)

# Confidence interval for estimated coefficients ----
# Use confint()
# View confidence intervals (default 95%)
confint(model)

