data(mtcars)

# Scale the data for better heatmap visuals
scaled_data <- scale(mtcars)

# Create heatmap
heatmap(scaled_data,
        col = colorRampPalette(c("blue", "white", "red"))(100),
        main = "Heatmap of mtcars (scaled)",
        margins = c(6, 10))
# Create cluster heatmap ----

# Adds dendograms to the heatmap
heatmap (scaled_data[1:10, ]) 

# Scale the data
heatmap(scaled_data[1:10, ], scale = "column")|

 # Create new heatmap with one dendogram
 heatmap (scaled_data[1:10, ], Colv = NA, scale = "column")


