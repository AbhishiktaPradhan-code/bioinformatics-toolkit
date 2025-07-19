
n = 29  # months
k = 2  

F = [0] * n
F[0] = 1
F[1] = 1

for i in range(2, n):
    F[i] = F[i-1] + k * F[i-2]

print(F[n-1])  