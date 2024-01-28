import pyperclip

String = input("Input string here: ")
Coordinates = input("Input coordinates here: ")
print(String)
print(Coordinates)
CoorList = Coordinates.split()
W1Start = int(CoorList[0])
W1End = int(CoorList[1])
W2Start = int(CoorList[2])
W2End = int(CoorList[3])
print("W1Start: " + str(W1Start))
print("W1End: " + str(W1End))
print("W2Start: " + str(W2Start))
print("W2End: " + str(W2End))

Result = f'{String[W1Start:W1End + 1]} {String[W2Start: W2End + 1]}'
print(Result)
pyperclip.copy(Result)