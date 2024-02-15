import pyperclip
result = 0

string_input = input("Input data here: ")
string_splice = string_input.split()
start = int(string_splice[0])
end = int(string_splice[1])

# for x in range(start,end + 1):
#     if x % 2 == 1:
#         result += x

result = sum(x for x in range(start,end + 1) if x % 2 == 1)

print(result)
pyperclip.copy(result)
    
