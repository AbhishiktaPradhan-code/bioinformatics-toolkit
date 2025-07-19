s="GAGCCTACTAACGGGAT"
t="CATCGTAATGACGGCCT"
count = 0
for c, d in zip(s, t):
    if c != d:
        count += 1
print(count)