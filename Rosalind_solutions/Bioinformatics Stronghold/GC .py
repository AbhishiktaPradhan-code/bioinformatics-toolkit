def parse_fasta(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    
    fasta_dict = {}
    label = ""
    for line in lines:
        if line.startswith('>'):
            label = line[1:].strip()
            fasta_dict[label] = ""
        else:
            fasta_dict[label] += line.strip()
    return fasta_dict

def gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / len(seq)) * 100

filename = 'rosalind_gc.txt'
fasta_seqs = parse_fasta(filename)

max_gc_id = ""
max_gc_value = 0

for seq_id, sequence in fasta_seqs.items():
    gc = gc_content(sequence)
    if gc > max_gc_value:
        max_gc_value = gc
        max_gc_id = seq_id

print(max_gc_id)
print(f"{max_gc_value:.6f}")