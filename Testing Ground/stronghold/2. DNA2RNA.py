import pyperclip
DNA = input("Input DNA here: ")
RNA = DNA.replace("T", "U")
print("-"*20)
print(RNA)
pyperclip.copy(RNA)