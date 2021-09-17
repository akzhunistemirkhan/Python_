# В мире ведьмака существуют монеты с номиналами 1, \, 5, \, 10, \, 251,5,10,25.
# минимально возможное количество чеканных монет для оплаты.
# 49 => 7     1 => 1    5 => 1
n = int(input())
print(n // 25 + n % 25 // 10 + n % 25 % 10 // 5 + n % 5)

#2
a=int(input())
total=0
while a!=0:
    if a>=25:
        total=total+1
        a-=25
    elif a>=10:
        total+=1
        a-=10
    elif a>=5:
        total+=1
        a-=5
    elif a>=1:
        total+=1
        a-=1
print(total)

#3
n = int(input())
k = 0
for i in (25, 10, 5, 1):
    while n // i > 0:
        k += 1
        n -= i
print(k)

#4
reward = int(input())
total = 0
for coin in [25, 10, 5, 1]:
    total += reward // coin
    reward %= coin 
print(total)