def reverse_complement(seq):
    
    complement_table = str.maketrans("ACGT", "TGCA")
    
   
    return seq[::-1].translate(complement_table)


Sequence = "AAAACCCGGT"


print(reverse_complement(Sequence))