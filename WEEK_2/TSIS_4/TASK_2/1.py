import re
n = input()
res = re.split(r',|\.', n)
for i in res:
    print(i)