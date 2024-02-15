from bio_struct import *
from random import choice
from collections import Counter

class bio_seq:
    def __init__(self, seq="ATCG", seq_type="DNA", label=None):
        """Sequence innit, validation"""
        if label is None:
            label = f"Seq#{id(self)}"
        self.seq = seq.upper()
        self.label = label
        self.length = len(self.seq)
        self.seq_type = seq_type
        self.type_is_valid = self._type_validate()
        assert self.type_is_valid, f"Invalid sequence type: {self.seq_type}"
        self.seq_is_valid = self._seq_validate()
        assert self.seq_is_valid, f"Provided {self.seq_type} sequence is incorrect: {self.seq}"

    def _type_validate(self):
        """Check if the sequence type is valid"""
        return self.seq_type in ["DNA", "RNA", "AA"]

    def _seq_validate(self):
        """Check if the input sequence is valid DNA sequence"""
        return set(TypeDict[self.seq_type]).issuperset(self.seq)

    def get_seq_info(self):
        """Return sequence info"""
        return f"{'-'*50}\n[Label]: {self.label}\n[Type]: {self.seq_type}\n[Length]: {self.length}\n[Sequence]: {self.seq}"

    def random(self, len=50, seq_type="DNA"):
        """Generate random sequence provided length"""
        rnd_seq = ''.join([choice(TypeDict[seq_type]) for nuc in range(len)])
        return self.__init__(rnd_seq, seq_type, f"Random#{id(self)}")

    def count_kmer(self):
        """Count how many k-mers in alphabetical order"""
        tmpFreqDict = dict(sorted(Counter(self.seq).items()))
        return ' '.join([f"{key}:{val} " for key, val in tmpFreqDict.items()])

    def transcription(self):
        """Convert DNA to RNA by replacing (T)hymine wuth (U)racil"""
        return self.seq.replace("T", "U")

    def rev_transcription(self):
        """Convert RNA to DNA by replacing (U)racil with (T)hymine"""
        return self.seq.replace("U", "T")

    def reverse_complementary(self):
        """Covert into reverse complementary sequence"""
        return self.seq.translate(ComplemetaryDict[self.seq_type])[::-1]

    def duplex(self):
        """Output a visualization of a unwound double helix, but with styles 😎"""
        Complementary_DNA_Strand = self.seq.translate(ComplemetaryDict[self.seq_type])
        return f"Busting Out Helix Style 😎\n5'-{self.seq}-3'\n   {''.join('|' for c in range(self.length))}\n3'-{Complementary_DNA_Strand}-5'"

    def gc_content(self, decimal=4, seq=None):
        """Output GC content (default 4 decimals)"""
        if seq is None:
            seq = self.seq
        return f'{round((seq.count("C") + seq.count("G")) / len(seq) * 100, decimal)}'

    def gc_splice_content(self, k=20, decimal=4):
        """Output GC content of each splice (default 20N per splice)"""
        ratios = []
        for i in range(0, self.length - int(k) + 1, int(k)):
            substr = self.seq[i:i + k]
            ratios.append(self.gc_content(decimal, substr))
        return ratios

    def translation(self, init_pos=0, seq=None, type="str"):
        """Convert sequence to polypeptide chain"""
        if seq is None:
            seq = self.seq
        result = [CodonDict[self.seq_type][seq[pos:pos +3]] for pos in range(init_pos, len(seq) - 2, 3)]

        if type == "str":
            return ''.join(n for n in result)
        else:
            return result

    def codon_usage(self, AA):
        """Acquire frequncy of each codon encoding given by the sequence"""
        tmpList = []
        for i in range(0 , self.length - 2, 3):
            if CodonDict[self.seq_type][self.seq[i:i + 3]] == AA:
                tmpList.append(self.seq[i:i +3])

        freqDict = dict(Counter(tmpList))
        totalWeight = sum(freqDict.values())
        for seq in freqDict:
            freqDict[seq] = round(freqDict[seq] / totalWeight, 2)
        return freqDict

    def reading_frame_gen(self):
        """Generate all 6 ORF of protein sequences"""
        Rseq = self.reverse_complementary()
        ORF = []
        ORF.append(self.translation(0))
        ORF.append(self.translation(1))
        ORF.append(self.translation(2))
        ORF.append(self.translation(0, Rseq))
        ORF.append(self.translation(1, Rseq))
        ORF.append(self.translation(2, Rseq))
        return ORF

    def aa_splicer(self, seq=None):
            """Return a list of plausible protein sequence from unedited protein sequence"""
            current_prot = []
            proteins = []
            if seq is None:
                aa_seq = self.seq
            else:
                aa_seq = seq

            for aa in aa_seq:
                current_prot.append(aa)
                if current_prot[0] == "M":
                    if current_prot[-1] == "_":
                        current_prot.remove("_")
                        proteins.append(''.join(a for a in current_prot))
                        current_prot.clear()
                else:
                    current_prot.clear()
            return proteins

    def orf_proteins_gen(self, init_pos=0, end_pos=0, ordered=True):
        """Return all plausible protein sequence from the 6 ORF"""

        if end_pos > init_pos:
            tmp_seq = bio_seq(self.seq[init_pos:end_pos], self.seq_type)
            ORF = tmp_seq.reading_frame_gen()
            del tmp_seq
        else:
            ORF = self.reading_frame_gen()

        aa_seq = []
        for RF in ORF:
            aa = self.aa_splicer(RF)
            for seq in aa:
                aa_seq.append(seq)

        if ordered:
            return sorted(aa_seq, key=len, reverse=True)
        return aa_seq