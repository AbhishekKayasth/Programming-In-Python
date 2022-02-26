# 20CS025 - Abhishek Kayasth
# GIT Link - https://github.com/20CS025Abhishek/Programming-In-Python.git

str = input("Input String : ")

# print(str.swapcase()) ## Shortcut

swap = "" # For storing ans

for i in range(len(str)):
    if(str[i].islower()):
        swap += str[i].upper()
    elif(str[i].isupper()):
        swap += str[i].lower()
    else:
        swap += str[i]

print()
print("Output: ")
print(swap)