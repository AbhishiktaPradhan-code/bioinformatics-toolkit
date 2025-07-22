def read_fasta(text):
    fasta = {}
    label = None
    for line in text.strip().split('\n'):
        if line.startswith('>'):
            label = line[1:]
            fasta[label] = ''
        else:
            fasta[label] += line.strip()
    return list(fasta.values())

def is_common_substring(sub, sequences):
    return all(sub in seq for seq in sequences)

def longest_common_substring(sequences):
    shortest_seq = min(sequences, key=len)
    length = len(shortest_seq)

    for l in range(length, 0, -1):  # Try lengths from longest to shortest
        for start in range(length - l + 1):
            candidate = shortest_seq[start:start + l]
            if is_common_substring(candidate, sequences):
                return candidate
    return ''  # Fallback if no common substring found


with open('rosalind_lcsm.txt') as f:
    fasta_text = f.read()
sequences = read_fasta(fasta_text)
print(longest_common_substring(sequences))
