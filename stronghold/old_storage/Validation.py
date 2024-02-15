from Sequences import *

#Validates sequence
def ValidateSeq(dna_seq):
    """Check if the input sequence is valid DNA sequence or not"""
    temp_seq = dna_seq.upper()
    for nuc in temp_seq:
        if nuc not in Nucleotides:
            return False
    return temp_seq
