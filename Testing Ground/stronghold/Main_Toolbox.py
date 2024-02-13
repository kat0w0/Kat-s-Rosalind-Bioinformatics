from random import choice
from pyperclip import copy
from Sequences import *
from Rosalind import *

ops = {
    "1": Count_Nuc_Freq,
    "2": DNA_to_RNA,
    "3": DNA_Reverse_Complementary,
    "4": DNA_Helix,
    "5": GC_Content_Reader,
    "6": GC_Subsec_Reader,
    "7": DNA_Translation,
    "8": RNA_Translation,
    "9": Codon_usage,
    "10": Reading_frame_Gen,
    "11": Motif_search,
    "12": ORF_Proteins_gen
}

fasta_ops = {
    "1": FASTA_GC_Convert,
    "2": FASTA_GC_Highest,
    "3": Consensus_search,
    "4": Overlap_graph
}

mendel = {
    "1": Mendel_first_law,
    "2": Mendel_average
}

wabbit = {
    "1": Pingala_sequence,
    "2": Wabbit2
}

def Choice():
    menu = {
    "1": DNA_mode,
    "2": FASTA_mode,
    "3": Wabbit_mode,
    "4": Mendel_mode,
    "5": Ham_distance
    }

    print("1 NucSeq; 2 FASTA; 3 Wabbit; 4 Mendel; 5 Hamming")
    Program_mode = input("Which mode would you choose? ")
    if Program_mode in menu:
        result = menu[Program_mode]()
        if result is not None:
            print("-" * 50)
            print(result)
            if not isinstance(result, (list, dict)) and input("Copy result? y/n ") == "y":
                copy(result)
    else:
        print("Invalid mode!")
        Choice()

Random_factor = 300

def DNA_mode():
    print('Enter "f" to input Sample.txt or None to generate a random sequence')
    inputStr = input("ENTER NUC STRING HERE: ")
    if inputStr == "":
        # Random Sequence Generator
        print("Random mode!")
        inputStr = ''.join([choice(DNA_Nucleotides)
                            for nuc in range(Random_factor)])
    elif inputStr == "f":
        with open("Sample.txt", "r") as f:
            inputStr = f.read()
    DNA_Val(inputStr)

def DNA_Val(inputStr):
    DNAStr = ValidateSeq(inputStr)
    if DNAStr != False:
        print("Valid DNA Sequence!")
        print("1 Count Nuc; 2 DNA2RNA; 3 ReverseComplement;\n4 DNA Helix; 5 GC ratio; 6 GC segmented;\n7 DNA Trans; 8 RNA Trans; 9 Condon usage;\n10 ORFGen; 11 Motif search; 12 ORF Protein Gen")
        Select_num = input("Selection number: ")
        if Select_num in ops:
            result = ops[Select_num](DNAStr)
            print("-" * 50)
            if isinstance(result, str):
                print(DNA_Colorization(result))
            else:
                print(result)
            if not isinstance(result, (list, dict)) and input("Copy result? y/n ") == "y":
                copy(result)
        else:
            print("Invalid Sequence Number!")
            DNA_Val(inputStr)
    else:
        print("Invalid DNA Sequence!")
        DNA_mode()

def FASTA_mode():
    print("1 Read FASTA; 2 Highest GC Content; 3 Consensus search; 4 Overap graph")
    Select_num = input("Selection number: ")
    if Select_num in fasta_ops:
        result = fasta_ops[Select_num]()
        return result
    else:
        print("Invalid Sequence Number!")
        FASTA_mode()

def Mendel_mode():
    print("1 First law; 2 Average")
    Select_num = input("Selection number: ")
    if Select_num in mendel:
        result = mendel[Select_num]()
        return result
    else:
        print("Invalid Sequence Number!")
        Mendel_mode()

def Wabbit_mode():
    print("1 Mortal; 2 Immortal")
    Select_num = input("Selection number: ")
    if Select_num in mendel:
        result = wabbit[Select_num]()
        return result
    else:
        print("Invalid Sequence Number!")
        Wabbit_mode()

if __name__ == "__main__":
    Choice()