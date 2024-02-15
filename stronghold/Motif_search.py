from Formats import Format_fasta
from Sequences import *

def Motif_search():
    FASTA = Format_fasta()
    print(f'Length of profile: {len(FASTA)}')
    Seq_list = list(FASTA.values())
    tmp_list = ["A", "T", "C", "G"]
    return Motif_loop(Seq_list, tmp_list)

# def Motif_loop(Seq_list, tmp_list):
#     while True:
#         for seq in tmp_list:
#             for nuc in ["A", "T", "C", "G"]:
#                 motif = seq + nuc
#                 if all(motif in s for s in Seq_list):
#                     tmp_list.append(motif)
#         return max(tmp_list, key=len)

def Motif_loop(Seq_list, tmp_list):
    motif = 'GGTACTTGGTCTCTCGTGTGTTGGGGGATATAAGTCTTTGCTCAGTTGGTGTATGAGGATGCAAAGACGGTGATAGTTTACACAACTCTGCGTCTTGCTCTAATGTATTATTCTCGATTGGTCCTCCTTATTGCACTAAGGGGGGCAACAGTACACC'
    print(all(motif in s for s in Seq_list))

print(Motif_search())