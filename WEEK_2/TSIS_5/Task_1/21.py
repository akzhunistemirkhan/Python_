n = int(input())
file = open("te.txt", "w")
al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0, 26, n):
    words = [al[i:i+n] + "\n"] 
    for word in words:
        file.write(word)