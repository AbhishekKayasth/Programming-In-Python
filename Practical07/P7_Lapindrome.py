# 20CS025 - Abhishek Kayasth
# GIT Link - https://github.com/20CS025Abhishek/Programming-In-Python.git

# Input test cases
n = int(input("Enter test case no: "))

sList = list()

for i in range(n):
    sList.append(input())

for i in range(n):
    s = sList[i]
    s1, s2 = '', ''

    if len(s) % 2 == 0:
        s1 = s[: len(s) // 2]
        s2 = s[len(s) // 2 :]
    else:
        s1 = s[: len(s) // 2]
        s2 = s[len(s) // 2 + 1 :]

    list1 = list(s1)
    list2 = list(s2)

    list1.sort()
    list2.sort()

    if str(list1) == str(list2):
        print("YES")
    else:
        print("NO")