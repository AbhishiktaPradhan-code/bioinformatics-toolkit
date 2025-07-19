s = "GATATATGCATATACTT"
t = "ATAT"

positions = []

for i in range(len(s) - len(t) + 1):
    if s[i:i+len(t)] == t:
        positions.append(i + 1)  # 1-based index

print(" ".join(map(str, positions)))