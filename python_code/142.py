import os
text = os.stat("my.txt")
print(text.st_size)