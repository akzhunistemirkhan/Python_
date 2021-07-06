str = []
file = ["my.txt", "your.txt"]
for words in file:
   file = open(words, 'r')
   str.append(file.read())
print(*str)