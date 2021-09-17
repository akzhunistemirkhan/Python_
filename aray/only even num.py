2                      # 1
4                      # 2 
6                      # 3      => NO
8                      # 4 
10                     #..
12      #=> YES           из 10 целых чисел и определяет является ли каждое из них четным или нет.
14

cnt = 0
for i in range(1,11):
    a=int(input())
    if a % 2 == 0:
        cnt+=1
if cnt == 10:
    print('YES')
else:
    print('NO')

#2
ok = True
for i in range(1,11):
    a = int(input())
    if a % 2 != 0:
        ok = False
if ok == True:
    print('YES')
else:
    print('NO')

#3
flag = 'YES'
for _ in range(10):
    a = int(input())
    if a % 2 != 0:
        flag = 'NO'
print(flag)

#4
answer = 'YES'
for _ in range (10):
    if int(input()) % 2:
        answer = 'NO'
        break
print(answer)




