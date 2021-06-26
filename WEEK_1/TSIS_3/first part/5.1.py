a = list(map(int, input().split()))
n = int(input())
lst = a[-n:] + a[:-n]
print(*lst)