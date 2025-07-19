Str = "We tried list and we tried dicts also we tried Zen"
dict = {}

for word in Str.split(' '):
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

# Now print the final counts
for word, count in dict.items():
    print(f"{word} {count}")