# 20CS025 - Abhishek Kayasth
# GIT Link - https://github.com/20CS025Abhishek/Programming-In-Python.git

# Words Input Count
n = int(input("Enter n: "))

print("Enter ", n, " words in next ", n, " lines: ")

# List for storing words
words = dict()

# Input word, if already exists, then increse count otherwise make new element
for i in range(n):
    word = input()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(len(words))

for i, j in words.items():
    print(j, end = " ")