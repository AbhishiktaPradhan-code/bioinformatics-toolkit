#Grammar of Graphics using ggplot2
#This script uses two packages: ggplot? and reshape2
# Install these two packages
# Load necessary packages
library(ggplot2)
library(reshape2)

# Load DNase dataset
data(DNase)

# Simulate: half as "Untreated", half as "Treated"
set.seed(123)  # for reproducibility

# Split original data in half and assign condition
untreated <- DNase
untreated$Condition <- "Untreated"

treated <- DNase
treated$Condition <- "Treated"

# Introduce a simulated effect: increase absorbance in "Treated"
treated$density <- treated$density + rnorm(nrow(treated), mean = 0.1, sd = 0.02)

# Combine both groups into one data frame
dnase_mod <- rbind(untreated, treated)

# View first few rows
head(dnase_mod)

#step 1
ggplot()

#step 2
ggplot(dnase_mod)

#step 3
ggplot(dnase_mod,aes(x=conc,y=density))

#step 4
ggplot(dnase_mod,aes(x=conc,y=density))+geom_point()

# Assign the plot to a variable
d1<- ggplot(dnase_mod,aes(x=conc,y=density))+geom_point()

d1

# Add line to scatter plot & create a new plot
p2<- d1 + geom_line()
p2

