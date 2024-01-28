import collections
import pyperclip

input = input("Input string here: ")
# WordDict = {}

# for word in input.split():
#     if word in WordDict:
#         WordDict[word] += 1
#     else:
#         WordDict[word] = 1

WordDict = collections.Counter(input.split(' '))


# output = dict(collections.Counter(input))
with open("DictOutput.txt", "w+") as f:
    for key, value in WordDict.items():
        Answer = f'{key} {value}'
        f.write(Answer + "\n")
    f.seek(0)
    Result = f.read()
    pyperclip.copy(Result[:-1])
    print(Result[:-1])