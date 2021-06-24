def palindrom(a):
    b = a[::-1]
    for i in range(len(a)):
        if b[i]!=a[i]:
            return False
    return True
a = input()
if palindrom(a):
    print("YES")
else:
    print(b[i],"NO")