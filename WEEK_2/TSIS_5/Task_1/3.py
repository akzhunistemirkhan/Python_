import os
File = open("my.txt", "w")
File.write(input())
File.close()
f = open("my.txt")
print(f.read())