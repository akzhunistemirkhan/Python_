#Fus              Fus
#Ro        =>     Ro 
#КОНЕЦ
#Dah          вывести все слово до "конец"

1)print(*[i for i in iter(input, 'КОНЕЦ')], sep='\n')

2)flag = true
  while flag == True:
    n = input()
    if n != 'КОНЕЦ':
        print(n)
    else:
        flag = False 

3)a = input()
while a != 'КОНЕЦ':
    print(a)
    a = input()
