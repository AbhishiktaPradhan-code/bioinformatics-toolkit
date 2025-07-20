
## Matrix ###

# ****************************************

# (1) Use matfix) function
# (2) use cbindo
# (3) use rbindo
# (4) Convert data frame to matrix
# *************************************** ~
# Matrix indexing


# create vector
d <- c(1:10)
# create matrix using the vector
m <- matrix(d, nrow = 2, ncol = 5, byrow = FALSE)
print(m)
# check the class
class (m)


# create two vectors
d <- c(1:10)
e <- c(21:30)

# bind the vectors as rows to form a matrix
m <- rbind(d, e)

# print the matrix
print(m)



# (4) Convert data frame to matrix ----

# Get the BOD dataset of R
d <- BOD
 # Check class
class (d)

# Convert to matrix
m <- data.matrix(d)
print(m)

# Matrix indexing -----

# matrix[row number, column number]

# print the value or element in row = 3, column = 2

print (m[3, 2])

# print the first column

print(m[ , 1])

# Transpose of a matrix ----

# Use t() function

mt <- t (m)
print(mt)


# Create two matrices

m <- matrix(c(1:4), nrow = 2, ncol = 2, byrow = TRUE)

n <- matrix(c(11:14), nrow = 2, ncol = 2, byrow = FALSE)
# Add two matrices

sum.mn <- m + n
print (sum.mn)


# Matrix multiplication ----

# scalar multiplication
sm <- 2*m

print (sm)


# Matrix-Matrix multiplication: use | opfrator
mm<- m %*% n
print (mm)
# Element-wise multiplication: matrix_1 * matrix_2

print(m*n)


# Use def function

print (det (m) )

# *************************************
 # Eigenvalues and eigen vectors

# Use eigen() function that returns both
ev <- eigen(m)

# Get the eigenvalues
values <- ev$values

print(values)

