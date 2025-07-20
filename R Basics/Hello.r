print(sqrt(16))
x <- seq(1, 10, 1)
print(x)
y <- x^2
print(y)
plot(x, y, type = "b", col = "blue", pch = 19, xlab = "x values", ylab = "y values (x^2)", main = "Plot of y = x^2")
# Save the plot to a file
dev.copy(png, "plot_x_squared.png")
dev.off()
