def Wabbit2():
    User_Input = input("Enter the (month)n and (lifespan)m values: ")
    User_Input = User_Input.split()
    month = int(User_Input[0])
    lifespan = int(User_Input[1])
    Pop = [0, 1]
    for itr in range(1, month + 1):
        print("Month: ",itr)
        if itr < lifespan:
            Pop.append(Pop[itr] + Pop[itr - 1])
        elif itr == lifespan:
            Pop.append(Pop[itr] + Pop[itr - 1] - Pop[itr - lifespan + 1])
        elif itr > lifespan:
            Pop.append(Pop[itr] + Pop[itr - 1] - Pop[itr - lifespan])
    return Pop[month]