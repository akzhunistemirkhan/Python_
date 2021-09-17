a = input().split()
for i in a:
    if i == ''.join(reversed(i)):
        a.remove(i)
print(a.sort())