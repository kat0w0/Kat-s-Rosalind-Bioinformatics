from Formats import Format_fasta

def GC_Content_Reader(DNAStr):
    """Output GC Content ratio in 3 decimals"""
    return f'{round((DNAStr.count("C") + DNAStr.count("G")) / len(DNAStr) * 100, 4)}'

def GC_Subsec_Reader(DNAStr):
    """Output GC Content ration of each subsections"""
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
    Temp_Dict = FASTA_GC_Convert()
    Largest_GC_Key = max(Temp_Dict, key=Temp_Dict.get)
    return f'{Largest_GC_Key}\n{Temp_Dict[Largest_GC_Key]}'[1:]