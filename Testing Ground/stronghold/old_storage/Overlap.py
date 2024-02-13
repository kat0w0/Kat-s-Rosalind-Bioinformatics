from Formats import Format_fasta
import pyperclip

def Overlap_graph(k=3):
    FASTA = Format_fasta()
    Seq_list = list(FASTA.values())
    Key_list = list(FASTA.keys())
    Result = []
    for i in range(len(FASTA)):
        # print(Seq_list[i], Seq_list[i][-k:])
        for n in range(len(FASTA)):
            # print(Seq_list[n], Seq_list[n][:k])
            if n != i and Seq_list[i][-k:] == Seq_list[n][:k]:
                Result.append(f"{Key_list[i][1:]} {Key_list[n][1:]}")
    return '\n'.join(Result)

# print(Overlap_graph(3))
pyperclip.copy(Overlap_graph(3))