coffee.data <- read.csv("/Users/abhishiktapradhan/Desktop/Bioinformatics roadmap/bioinformatics-summer/R Basics/coffee.csv", header = TRUE)
print(coffee.data)

ages <- c(23, 34, 35, 29, 41, 42, 30, 22, 40, 30)
sys <- c(122, 120, 120, 115, 130, 131, 118, 122, 120, 115)
dia <- c(83, 79, 78, 72, 90, 90, 82, 80, 82, 75)
print(ages)
length(sys)
min(sys)
max(sys)
median (sys)
mean (sys)
var (sys)
sd (sys)

bp.data <- data.frame(ages, sys, dia)

summary (bp.data)


hist(sys)
