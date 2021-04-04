#Вывести в обратном порядке
a = input().split()
for i in range(0,len(a)):
    n_list = list(a)
    n_list.reverse()
print(*n_list)
