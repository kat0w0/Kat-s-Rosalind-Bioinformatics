def Mendel_first_law():
    Pop = input("Input the three genotypical freq seperated by spaces(k m n): ")
    Pop = Pop.split()
    Dom = int(Pop[0])
    Het = int(Pop[1])
    Res = int(Pop[2])
    Total_pop = Dom + Het + Res
    Dom_Dom = (Dom / Total_pop) * ((Dom - 1) / (Total_pop - 1)) * 1
    Dom_Het = (Dom / Total_pop) * (Het / (Total_pop - 1)) * 1
    Dom_Res = (Dom / Total_pop) * (Res / (Total_pop - 1)) * 1
    Het_Dom = (Het / Total_pop) * (Dom / (Total_pop - 1)) * 1
    Het_Het = (Het / Total_pop) * ((Het - 1) / (Total_pop - 1)) * 0.75
    Het_Res = (Het / Total_pop) * (Res / (Total_pop - 1)) * 0.5
    Res_Dom = (Res / Total_pop) * (Dom / (Total_pop - 1)) * 1
    Res_Het = (Res / Total_pop) * (Het / (Total_pop - 1)) * 0.5
    Res_Res = (Res / Total_pop) * ((Res - 1) / (Total_pop - 1)) * 0
    P_Total = [Dom_Dom, Dom_Het, Dom_Res, Het_Dom, Het_Het, Het_Res, Res_Dom, Res_Het, Res_Res]
    Result = sum(P_Total)
    return Result

