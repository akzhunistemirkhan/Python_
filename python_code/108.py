#которая выводит номера элементов массива, равных данному числу.
n = int(input())
a = list(map(int,input().split()))
k = int(input())
for i in range(n):
    if a[i]==k:
        print(i+1)