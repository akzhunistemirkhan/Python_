n = int(input())
file = open("my.txt","r")
f = file.readlines()
text = f[-n:]
print(*text)