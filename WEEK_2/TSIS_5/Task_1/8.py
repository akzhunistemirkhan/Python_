file = open("my.txt","r")
str = file.read().split()
maxlenght = len(max(str, key = len))
for word in str:
    if len(word) == maxlenght:
        print(word)