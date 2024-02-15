def Format_fasta():
    with open('FASTA.txt', 'r') as f:
        FASTA_Sample = [lines.strip() for lines in f.readlines()]

        FASTA_Dict = {}
        FASTA_Label = ""

        for line in FASTA_Sample:
            if '>' in line:
                FASTA_Label = line
                FASTA_Dict[FASTA_Label] = ""
            else:
                FASTA_Dict[FASTA_Label] += line

    return FASTA_Dict