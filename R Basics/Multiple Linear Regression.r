# Multiple Linear Regression

#y= a + b1.x1 + b2.x2 + b3.x3 + ....

# for Linear Regression

data(mtcars)
head(mtcars)

# Fit multiple linear regression model
model2 <- lm(mpg ~ wt + hp, data = mtcars)

# Summary of the model
summary(model2)


confint(model2)
  
