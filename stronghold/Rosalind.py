from collections import Counter
from Sequences import *
from Formats import Format_fasta


#Validates sequence
def ValidateSeq(dna_seq):
    """Check if the input sequence is valid DNA sequence or not"""
    temp_seq = dna_seq.upper()
    for nuc in temp_seq:
        if nuc not in Nucleotides and nuc not in ["\n"]:
            return False
    return temp_seq

def Count_Nuc_Freq(seq):
    """Count how many nucleotides in the order of A T C G"""
    tmpFreqDict = dict(sorted(Counter(seq).items()))
    print(tmpFreqDict)
    resultstr = ' '.join([str(val) for key, val in tmpFreqDict.items()])
    return resultstr

def DNA_to_RNA(DNA):
    """Convert DNA to RNA by replacing (T)hymine wuth (U)racil"""
    RNA = DNA.replace("T", "U")
    return RNA

def DNA_Reverse_Complementary(DNA):
    """Output the complementary sequence"""
    ReverseDNA = DNA.translate(Pythonic_DNA_Complements)[::-1]
    return ReverseDNA

def DNA_Helix(DNA):
    """Output a visualization of a unwound DNA helix, but with styles 😎"""
    Complementary_DNA_Strand = DNA.translate(Pythonic_DNA_Complements)
    StylizedDNA = f"Busting Out Helix Style 😎\n5'-{DNA}-3'\n   {''.join('|' for c in range(len(DNA)))}\n3'-{Complementary_DNA_Strand}-5'" 
    return StylizedDNA

def GC_Content_Reader(DNAStr):
    """Output GC Content ratio in 3 decimals"""
    return f'{round((DNAStr.count("C") + DNAStr.count("G")) / len(DNAStr) * 100, 4)}'

def GC_Subsec_Reader(DNAStr):
    """Output GC Content ratio of each subsections"""
    k = input("Input subsec length (Default is 20): ")
    if k == "":
        k = 20

    ratios = []
    for i in range(0, len(DNAStr) - int(k) + 1, int(k)):
        substr = DNAStr[i:i + k]
        ratios.append(GC_Content_Reader(substr))
    return ratios

def FASTA_GC_Convert():
    """Convert all FASTA seq into GC Content ratio"""
    Result_Dict = {key: GC_Content_Reader(value) for (key, value) in Format_fasta().items()}
    return Result_Dict

def FASTA_GC_Highest():
    """Output the profile with the highest GC Content ratio"""
    Temp_Dict = FASTA_GC_Convert()
    Largest_GC_Key = max(Temp_Dict, key=Temp_Dict.get)
    return f'{Largest_GC_Key}\n{Temp_Dict[Largest_GC_Key]}'[1:]

def Pingala_sequence():
    """Rate of rabbit reproducing and taking over the world"""
    User_Input = input("Enter the (month)n and (birth_rate)k values: ")
    User_Input = User_Input.split()
    month = int(User_Input[0])
    birth_rate = int(User_Input[1])
    parent, child = 1, 1
    for itr in range(month - 1):
        child, parent = parent, parent + (child * birth_rate)
    return child

def Wabbit2():
    User_Input = input("Enter the (month)n and (lifespan)m values: ")
    User_Input = User_Input.split()
    month = int(User_Input[0])
    lifespan = int(User_Input[1])
    Pop = [0, 1]
    for itr in range(1, month + 1):
        if itr < lifespan:
            Pop.append(Pop[itr] + Pop[itr - 1])
        elif itr == lifespan:
            Pop.append(Pop[itr] + Pop[itr - 1] - Pop[itr - lifespan + 1])
        elif itr > lifespan:
            Pop.append(Pop[itr] + Pop[itr - 1] - Pop[itr - lifespan])
    return Pop[month]

def Ham_distance():
    seq1 = input("First seqeunce: ")
    seq2 = input("Second seqeunce: ")
    result = sum(nuc1 != nuc2 for nuc1, nuc2 in zip(seq1, seq2))
    return result

def DNA_Translation(DNAStr, init_pos=0):
    """Return the translated amino acid chain from DNA Strings"""
    return [DNA_Codons[DNAStr[pos:pos +3]] for pos in range(init_pos, len(DNAStr) - 2, 3)]

def RNA_Translation(RNAStr, init_pos=0):
    """Return the translated amino acid chain from RNA Strings"""
    Result = [RNA_Codons[RNAStr[pos:pos +3]] for pos in range(init_pos, len(RNAStr) - 2, 3)]
    return "".join(str(val) for val in Result)

def Motif_search(Str, Motif=None):
    """Search a motif in a given Nuc string"""
    Pos = []
    if Motif is None:
        Split_str = Str.split('\n')
        Nuc_str = Split_str[0]
        Motif = Split_str[1]
    for i in range(0, len(Nuc_str) + 1):
        if Motif == Nuc_str[i:i + len(Motif)]:
            Pos.append(i + 1)
    return " ".join(str(num) for num in Pos)

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
    # print("-" * 50)
    # print(freqDict)
    return freqDict

def Reading_frame_Gen(DNAStr):
    """Generate all 6 ORF in a sequence"""
    RDNAStr = DNA_Reverse_Complementary(DNAStr)
    ORF = []
    ORF.append(DNA_Translation(DNAStr, 0))
    ORF.append(DNA_Translation(DNAStr, 1))
    ORF.append(DNA_Translation(DNAStr, 2))
    ORF.append(DNA_Translation(RDNAStr, 0))
    ORF.append(DNA_Translation(RDNAStr, 1))
    ORF.append(DNA_Translation(RDNAStr, 2))
    return ORF

def Mendel_first_law():
    """Find the probability of a phenotypically dominant offspring"""
    Pop = input("Input the three genotypical freq seperated by spaces(k m n): ")
    Pop = Pop.split()
    Dom = int(Pop[0])
    Het = int(Pop[1])
    Res = int(Pop[2])
    Total_pop = Dom + Het + Res
    Dom_Dom = (Dom / Total_pop) * ((Dom - 1) / (Total_pop - 1)) * 1
    Dom_Het = (Dom / Total_pop) * (Het / (Total_pop - 1)) * 1
    Dom_Res = (Dom / Total_pop) * (Res / (Total_pop - 1)) * 1
    Het_Dom = (Het / Total_pop) * (Dom / (Total_pop - 1)) * 1
    Het_Het = (Het / Total_pop) * ((Het - 1) / (Total_pop - 1)) * 0.75
    Het_Res = (Het / Total_pop) * (Res / (Total_pop - 1)) * 0.5
    Res_Dom = (Res / Total_pop) * (Dom / (Total_pop - 1)) * 1
    Res_Het = (Res / Total_pop) * (Het / (Total_pop - 1)) * 0.5
    Res_Res = (Res / Total_pop) * ((Res - 1) / (Total_pop - 1)) * 0
    P_Total = [Dom_Dom, Dom_Het, Dom_Res, Het_Dom, Het_Het, Het_Res, Res_Dom, Res_Het, Res_Res]
    Result = sum(P_Total)
    return Result

def Mendel_average():
    """Find the average of a phenotypically dominant offspring"""
    Pop = input("Input the 6 different couple pairings seperated by spaces: ")
    Pop = Pop.split()
    Dom_Dom = int(Pop[0])
    Dom_Het = int(Pop[1])
    Dom_Res = int(Pop[2])
    Het_Het = int(Pop[3]) * 0.75
    Het_Res = int(Pop[4]) * 0.5
    # Res_Res = int(Pop[5]) * 0
    Result = Dom_Dom + Dom_Het + Dom_Res + Het_Het + Het_Res
    return Result * 2

def Consensus_search():
    """Output the profile with the highest GC Content ratio"""
    FASTA = Format_fasta()
    FASTA_amount = len(FASTA)
    Seq_list = list(FASTA.values())
    Consensus_seq = []
    Adenosine = []
    Thymine = []
    Cytosine = []
    Guanine = []
    Nuc_name = {
    'A': Adenosine,
    'T': Thymine,
    'C': Cytosine,
    'G': Guanine
    }
    for nuc in range(min(map(len, Seq_list))):
        tmp_list = []
        for i in range(FASTA_amount):
            tmp_list.append(Seq_list[i][nuc])
        tmp_dict = dict(Counter(tmp_list))
        for nucleotide in DNA_Nucleotides:
            Nuc_name[nucleotide].append(tmp_dict.get(nucleotide, 0))
        max_value = Counter(tmp_list).most_common(1)[0][0]
        Consensus_seq.append(max_value)

    return f"{''.join(n for n in Consensus_seq)}\nA: {' '.join(str(a) for a in Adenosine)}\nC: {' '.join(str(c) for c in Cytosine)}\nG: {' '.join(str(g) for g in Guanine)}\nT: {' '.join(str(t) for t in Thymine)} "

def Overlap_graph(k=3):
    FASTA = Format_fasta()
    Seq_list = list(FASTA.values())
    Key_list = list(FASTA.keys())
    Result = []
    for i in range(len(FASTA)):
        for n in range(len(FASTA)):
            if n != i and Seq_list[i][-k:] == Seq_list[n][:k]:
                Result.append(f"{Key_list[i][1:]} {Key_list[n][1:]}")
    return '\n'.join(Result)

def AA_splicer(aa_seq):
        """Compute all possible proteins in an aminoacid seq and return a list of possible proteins"""
        current_prot = []
        proteins = []
        for aa in aa_seq:
            current_prot.append(aa)
            if current_prot[0] == "M":
                if current_prot[-1] == "_":
                    current_prot.remove("_")
                    proteins.append(''.join(a for a in current_prot))
                    current_prot = []
            else:
                current_prot = []
        return proteins

def ORF_Proteins_gen(Seq, init_pos=0, end_pos=0, ordered=True):
    """Generate all possible protein seq from the 6 ORF"""

    if end_pos > init_pos:
        ORF = Reading_frame_Gen(Seq[init_pos:end_pos])
    else:
        ORF = Reading_frame_Gen(Seq)

    AA_Seq = []
    for RF in ORF:
        AA = AA_splicer(RF)
        for seq in AA:
            AA_Seq.append(seq)

    if ordered:
        return sorted(AA_Seq, key=len, reverse=True)
    return AA_Seq