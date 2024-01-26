import pyperclip

DNA = input("DNA String here: ")
DNA = list(DNA)
DNA.reverse()
ReverseDNA = "".join(DNA)
print(ReverseDNA)
ReverseDNA = ReverseDNA.lower()
ReverseDNA = ReverseDNA.replace("a", "T")
ReverseDNA = ReverseDNA.replace("t", "A")
ReverseDNA = ReverseDNA.replace("c", "G")
ReverseDNA = ReverseDNA.replace("g", "C")
print(ReverseDNA)
pyperclip.copy(ReverseDNA)