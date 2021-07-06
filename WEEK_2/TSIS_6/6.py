def function(a, b, n):
    if a <= n and n <= b:
        return True
    else: return False
a, b = map(int, input().split())
n = int(input())
if function(a, b, n):
    print('YES')
else:
    print('NO')