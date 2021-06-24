def function(a,b,n):
    if n>=a and n<=b:
        return True
    else:
        return False
a,b,n = map(int,input().split())
if function(a,b,n):
    print('YES')
else:
    print('NO')