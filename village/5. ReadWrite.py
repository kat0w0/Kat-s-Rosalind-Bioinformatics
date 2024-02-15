import pyperclip
import linecache

with open("/home/kat/Documents/Bioinformatics/Testing Ground/village/Sample.txt", 'r') as f:
    Totallines = len(f.readlines()) + 1

f = open('Output.txt', 'w')
for x in range(1, Totallines):
    if x % 2 == 0:
        read = linecache.getline("Sample.txt", x)
        result = read[:-1]
        #print(result)
        f.write(result + "\n")

f.close()

with open("Output.txt", 'r') as f:
    Answer = f.read()
    pyperclip.copy(Answer[:-1])

# Output = []
# with open("/home/kat/Documents/Bioinformatics/Testing Ground/village/Sample.txt", "r") as f:
#     Output = [line for pos, line in enumerate(
#         f.readlines()) if pos % 2 != 0]
    
# with open("Output.txt", "w") as f:
#     f.write("".join([line for line in Output]))