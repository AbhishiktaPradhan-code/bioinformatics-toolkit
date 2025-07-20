data("USArrests")
head(USArrests)
km <- kmeans(USArrests, centers = 3)
plot(USArrests, col = km$cluster)

# Scale the data
scaled_data <- scale(USArrests)

# Perform PCA
pca <- prcomp(scaled_data)

# Run K-means again on scaled data
km <- kmeans(scaled_data, centers = 3)

# Plot the first two principal components
plot(pca$x[, 1:2], col = km$cluster, pch = 19,
     xlab = "PC1", ylab = "PC2", main = "K-means Clustering on USArrests (PCA view)")

