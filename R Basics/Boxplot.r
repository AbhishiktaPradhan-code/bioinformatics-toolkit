data(PlantGrowth)
boxplot(weight ~ group, data = PlantGrowth,
        col = "orange",
        main = "Plant Weight by Group",
        xlab = "Group",
        ylab = "Weight")
