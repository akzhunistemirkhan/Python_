# 2514 => 12

#1
a = int(input())
sum = 0
while a!=0:
    x = a % 10
    sum += x
    a = a // 10
print(sum)

#2
a = input()
s = 0
for i in a:
    s += int(i)
print(s)

#3
print(sum(int(i) for i in input()))

#4
s = input()
summ = 0
for i in range(len(s)):
    summ += int(s[i])
print(summ)

#5
print(sum(map(int, input())))
