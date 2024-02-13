# from collections import Counter
from Sequences import *

def countNucFrequency(seq):
    """Count how many nucleotides in the order of A T C G"""
    # return dict(collections.Counter(seq))
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    print(tmpFreqDict)
    resultstr = ' '.join([str(val) for key, val in tmpFreqDict.items()])
    return resultstr