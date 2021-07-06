n = int(input())
with open(r'my.txt','r') as f:
    for line in range(n):
        print(f.readline(), end='')