import re
pattern = "[789]\d{9}"
n = int(input())
a = []
for i in range(n):
    str = input()
    if re.search(pattern, str) and len(str) == 10:
        a.append("YES")
    else:
        a.append("NO")
for i in a:
    print(i)
