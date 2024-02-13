import pyperclip

def Mendel_average():
    """Find the average of a phenotypically dominant offspring"""
    Pop = input("Input the 6 different couple pairings seperated by spaces: ")
    Pop = Pop.split()
    Dom_Dom = int(Pop[0])
    Dom_Het = int(Pop[1])
    Dom_Res = int(Pop[2])
    Het_Het = int(Pop[3]) * 0.75
    Het_Res = int(Pop[4]) * 0.5
    # Res_Res = int(Pop[5]) * 0
    Result = Dom_Dom + Dom_Het + Dom_Res + Het_Het + Het_Res
    pyperclip.copy(Result * 2)
    return Result * 2

print(Mendel_average())
