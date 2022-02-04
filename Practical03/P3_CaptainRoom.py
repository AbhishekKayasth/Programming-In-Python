# 20CS025 - Abhishek Kayasth
# GIT Link - 

print("Input : ")
k = int(input())
input_str = input()
lst = input_str.split()

print("Output : ")
for i in range(0, len(lst)):
    if(lst.count(lst[i]) != k):
        print(lst[i])