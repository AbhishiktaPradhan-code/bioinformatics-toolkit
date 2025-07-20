data(DNase)
head(DNase)
# Nonlinear model
nls_model <- nls(density ~ Vmax * conc / (Km + conc),
                 data = DNase,
                 start = list(Vmax = 1, Km = 0.5))

# Summary
summary(nls_model)

# Plot raw data
plot(DNase$conc, DNase$density,
     main = "Nonlinear Regression - Michaelis-Menten",
     xlab = "Concentration",
     ylab = "Density",
     pch = 19, col = "darkblue")

# Add curve
curve(coef(nls_model)[["Vmax"]] * x / (coef(nls_model)[["Km"]] + x),
      col = "red", lwd = 2, add = TRUE)

# Fit a quadratic model using lm()
poly_model <- lm(density ~ conc + I(conc^2), data = DNase)

# View model summary
summary(poly_model)

# Scatterplot
plot(DNase$conc, DNase$density,
     main = "Polynomial Regression (Quadratic)",
     xlab = "Concentration",
     ylab = "Density",
     pch = 19, col = "blue")

# Add quadratic curve
curve(predict(poly_model, newdata = data.frame(conc = x)),
      add = TRUE, col = "red", lwd = 2)


# Fit a quadratic (2nd-degree) polynomial model using poly()
# Set raw = TRUE to get the actual powers (not orthogonal polynomials)

md2 <- lm(density ~ poly(conc, 2, raw = TRUE), data = DNase)

# View the summary
summary(md2)


# Step 1: Fit the polynomial regression model
md2 <- lm(density ~ poly(conc, 2, raw = TRUE), data = DNase)

# Step 2: Create a smooth sequence of x values (conc values)
xv <- seq(min(DNase$conc), max(DNase$conc), by = 0.1)

# Step 3: Predict density using the model
yv <- predict(md2, newdata = data.frame(conc = xv), type = "response")

# Step 4: Plot the original data
plot(DNase$conc, DNase$density,
     main = "Polynomial Fit (Degree 2)",
     xlab = "Concentration",
     ylab = "Density",
     pch = 19, col = "blue")

# Step 5: Add the fitted curve
lines(xv, yv, col = "red", lwd = 2)
