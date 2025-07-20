# (1) Create vector using c() ----
u <- c(1, 3, 5, 7, 9)
print (u)


# (2) Create a vector using seq() ----
v <- seq(12, 46, 8)
print(v)

# Vector indexing -----

# vactor_name[element number]

# Get the third element of u:

print(u[3])

# Addition of vector to scalar -----
# Add 2 to vector u
  
p<- u + 2
print (p) 


# Add two vectors u and v
a <- u + V
print(a)


# Multiply vector v by 2
q <-2*V
print (q)


# Use dot of the 'geometry" library
# Install geometry library and load it before using dot
library (geometry)

# Calculate dot product of u and v
b <- dot (u, v)
print (b)


# Norm, Unit vector, and angle between vectors
# Magnitude of a vector ----
# Using norm()
# Get the magnitude of vector u by norm) function
x <- norm(u, type="2")
print (x)

# Get the unit vector of u
i <- u/norm(u, type="2")
print (i)

# Check the magnitude of the unit vector i
print(norm(i, type="2"))


# cos(theta) = (flot product of v1 & v2)/(norm of v1 * norm of v2)
# acos () calculates the cos inverse

theta <- acos (dot (u, v) /(norm(u, type="2") *norm(v, type="2")))

print (theta)


