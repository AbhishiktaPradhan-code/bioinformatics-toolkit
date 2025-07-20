# Read a csv file ----

coffee.data <- read.csv("/Users/abhishiktapradhan/Desktop/Bioinformatics roadmap/bioinformatics-summer/R Basics/coffee.csv", header = TRUE)
print(coffee.data)

head(coffee.data)
tail(coffee.data)

names(coffee.data)

dim(coffee.data)

nrow(coffee.data)

ncol(coffee.data)

str(coffee.data)

units_sold <- coffee.data$Units.Sold

units_sold[4]

d2 <- coffee.data[ ,2]

d23 <- coffee.data[ ,2:3]

data()

bod.data <- BOD
# Check part of the data
# Check name of variables
# Check dimension of the data
# Check structure of the data using str() function 
# Extract data using variable name and $ operator
# Extract one column using row and column number
# Extract part of the data using subset() function