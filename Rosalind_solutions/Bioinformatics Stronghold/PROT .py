amino_acid_codon = {
    'UUU': 'F', 'UUC': 'F',
    'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    
    'UAU': 'Y', 'UAC': 'Y',
    'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop',
    
    'CAU': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    
    'AAU': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K',
    
    'GAU': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    
    'UGU': 'C', 'UGC': 'C',
    'UGG': 'W',
    
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGA': 'R', 'AGG': 'R',
    
    'AGU': 'S', 'AGC': 'S',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}
input_sequence = "AUGGACUCCCGUGAUAUAUGGGGAAGCUGUCUUGCACAGUUGCCAUGGCUGGAUCUAACGUCUGCCAAUGUGGGUGA"
Translated_protein = ''
for i in range(0, len(input_sequence), 3):
    codon = input_sequence[i:i+3]
    if codon in ['UAA', 'UAG', 'UGA'] or amino_acid_codon.get(codon) == 'Stop':
        break
    elif codon in amino_acid_codon:
        Translated_protein += amino_acid_codon[codon]

print(Translated_protein)
# This code translates a given RNA sequence into a protein sequence.