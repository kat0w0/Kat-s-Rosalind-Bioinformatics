import pyperclip

num1 = int(input("number 1:"))
num2 = int(input("number 2s:"))

num3 = num1**2 + num2**2
num4 = pow(num1, 2) + pow(num2, 2)
print(num3)
print(num4)

if num3 == num4:
    pyperclip.copy(num3)
