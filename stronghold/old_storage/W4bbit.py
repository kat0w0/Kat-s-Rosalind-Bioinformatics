def Pingala_sequence():
    """Rate of rabbit reproducing and taking over the world"""
    User_Input = input("Enter the (month)n and (birth_rate)k values: ")
    User_Input = User_Input.split()
    month = int(User_Input[0])
    birth_rate = int(User_Input[1])
    parent, child = 1, 1
    for itr in range(month - 1):
        child, parent = parent, parent + (child * birth_rate)
    return child

    
