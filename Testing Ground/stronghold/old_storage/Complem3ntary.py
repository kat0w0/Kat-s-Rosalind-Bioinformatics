# import pyperclip
from Sequences import *

# DNA = input("DNA String here: ")
# DNA = list(DNA)
# DNA.reverse()
# ReverseDNA = "".join(DNA)
# print(ReverseDNA)
# ReverseDNA = ReverseDNA.lower()
# ReverseDNA = ReverseDNA.replace("a", "T")
# ReverseDNA = ReverseDNA.replace("t", "A")
# ReverseDNA = ReverseDNA.replace("c", "G")
# ReverseDNA = ReverseDNA.replace("g", "C")

def DNA_Complementary_function(DNA):
    """Output the complementary sequence"""
    # DNA_Upper = DNA.upper()[::-1]
    # ReverseDNA = DNA_Colorization(''.join([DNA_Complements[nuc] for nuc in DNA_Upper]))
    ReverseDNA = DNA.translate(Pythonic_DNA_Complements)[::-1]
    return ReverseDNA

def DNA_Helix(DNA):
    """Output a visualization of a unwound DNA helix, but with styles 😎"""
    # Complementary_DNA_Strand = ''.join([DNA_Complements[nuc] for nuc in DNA.upper()])
    Complementary_DNA_Strand = DNA.translate(Pythonic_DNA_Complements)
    StylizedDNA = f"Busting Out Helix Style 😎\n5'-{DNA}-3'\n   {''.join('|' for c in range(len(DNA)))}\n3'-{Complementary_DNA_Strand}-5'" 
    return StylizedDNA

# print(ReverseDNA)
# pyperclip.copy(ReverseDNA)