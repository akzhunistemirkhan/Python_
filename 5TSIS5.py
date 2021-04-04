#1
import os
def file_text(name):
        txt = open(name)
        print(txt.read())
file_text('my.txt')

#3
import os
File = open("my.txt", "w")
File.write("key")
File.write("word")
File.close()
txt = open("my.txt")
print(txt.read())

#4
file = open("my.txt","r")
text = file.readlines()
t_text = text[-1:]
print(t_text)

#5
file = open("my.txt","r")
text = file.readlines()
print(text)
print(type(text))

#8
file = open("my.txt","r")
words = file.read().split()
maxi = len(max(words, key=len))
for i in words:
    if len(i) == maxi:
        print(i)
        
#9
file = open("my.txt")
count = 0
for i in file:
    count += 1
print(count)

#10
import collections
file = open("my.txt")
print(*collections.Counter(file))

#11
import os
text = os.stat("my.txt")
print(text.st_size)



