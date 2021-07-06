import os
ans = os.stat("my.txt")
print(ans.st_size)