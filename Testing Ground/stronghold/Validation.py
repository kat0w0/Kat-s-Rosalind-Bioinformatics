# import collections
Nucleotides = ["A", "T", "C", "G"]


#Validates sequence
def ValidateSeq(dna_seq):
    temp_seq = dna_seq.upper()
    for nuc in temp_seq:
        if nuc not in Nucleotides:
            return False
    return temp_seq

def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
    # return dict(collections.Counter(seq))