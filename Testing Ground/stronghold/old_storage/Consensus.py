from Formats import *
from Sequences import *
from collections import Counter

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

print(Consensus_search())
