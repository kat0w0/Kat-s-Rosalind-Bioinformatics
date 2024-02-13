from Sequences import *
from collections import Counter

def DNA_Translation(DNAStr, init_pos=0):
    """Return the translated amino acid chain from DNA Strings"""
    print("-" * 50) 
    print([DNA_Codons[DNAStr[pos:pos +3]] for pos in range(init_pos, len(DNAStr) - 2, 3)])

def Codon_usage(DNAStr):
    """Provide frequncy for each coding encoding given a aminoacid in a DNA Sequence"""
    AA = input("Enter which amino acid (letter): ")
    tmpList = []
    for i in range(0 , len(DNAStr) - 2, 3):
        if DNA_Codons[DNAStr[i:i + 3]] == AA:
            tmpList.append(DNAStr[i:i +3])
    
    freqDict = dict(Counter(tmpList))
    totalWeight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWeight, 2)
    print("-" * 50)
    print(freqDict)