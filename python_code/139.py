#maxword in text
file = open("my.txt","r")
words = file.read().split()
maxi = len(max(words, key=len))
for i in words:
    if len(i) == maxi:
        print(i)
