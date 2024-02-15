from Rosalind import Reading_frame_Gen, DNA_Translation

def ORF_Proteins(Seq, init_pos=0, end_pos=0, ordered=False):
    """Generate all possible protein seq from the 6 ORF"""
    if end_pos > init_pos:
        ORF = Reading_frame_Gen(Seq)[init_pos:end_pos]
    else:
        ORF = Reading_frame_Gen(Seq)

    AA_Seq = []
    for RF in ORF:
        AA = DNA_Translation(RF)
        for seq in AA:
            AA_Seq.append(seq)

    if ordered:
        return sorted(AA_Seq, key=len, reverse=True)
    return AA_Seq