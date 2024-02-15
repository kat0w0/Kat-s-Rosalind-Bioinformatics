def Ham_distance():
    seq1 = input("First seqeunce: ")
    seq2 = input("Second seqeunce: ")
    result = sum(nuc1 != nuc2 for nuc1, nuc2 in zip(seq1, seq2))
    return result