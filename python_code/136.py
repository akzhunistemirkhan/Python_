import os
File = open("my.txt", "w")
File.write("key")
File.write("word")
File.close()
txt = open("my.txt")
print(txt.read())