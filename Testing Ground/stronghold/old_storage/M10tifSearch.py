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
