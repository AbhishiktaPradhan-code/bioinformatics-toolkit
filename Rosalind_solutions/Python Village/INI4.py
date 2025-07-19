a=100
b=200
c=0
for i in range(a, b+1):
    if i % 2 == 1:
        c+=i
    else:
        continue
print(c)  