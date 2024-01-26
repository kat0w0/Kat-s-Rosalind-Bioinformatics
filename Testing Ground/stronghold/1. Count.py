from Validation import *
import random
import pyperclip


def rndDNA():
    #rndDNAStr = "ATATATTATTTTGGCGCGGCGstgtgtgtgtC"

    rndDNAStr = ''.join([random.choice(Nucleotides)
                        for nuc in range(100)])
    return rndDNAStr

def inputDNA():
    inputDNAStr = input("DNA STRING HERE:")
    return inputDNAStr

confirmation = input("Input DNA Seq? y/n")
if confirmation == "y":
    unvalDNAStr = inputDNA()
    print("Input mode")
else:
    unvalDNAStr = rndDNA()
    print("Random mode")


DNAStr = ValidateSeq(unvalDNAStr)
if DNAStr is not False:
    result = countNucFrequency(DNAStr)
    print(result)
    print(type(result))
    resultstr = ' '.join([str(val) for key, val in result.items()])
    print(resultstr)
    pyperclip.copy(resultstr)
else:
    print("Invalid DNA String!")