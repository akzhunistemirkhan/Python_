a = input().split()
num = 1001
for i in range(len(a)):
    if i > 0 and i < num:
        num = i
print(num)