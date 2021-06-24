#количество цифр > цифры >  выводим сумму чисел
#5
#3
#2     =>  5     [3+2+1+0-1 = 5]
#1
#0
#-1
n = int(input())
total = 0
for i in range(n):
    a = int(input())
    total += a
print(total)