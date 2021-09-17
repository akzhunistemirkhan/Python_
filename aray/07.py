import math
a = int(input('“Please, input sides for triangle”:'))
b = int(input())
c = int(input())
d = int(input('“Please, input 2 sides for rectangle”:'))
e = int(input())
f = int(input('“Please, input radius for circle”:'))
circle = math.pi*f*f
rect = d*e
p= (a+b+c)/2
triang= math.sqrt(p*(p-a)*(p-b)*(p-c))
print('“The areas are: Circle=',round(circle,3),',Triangle=',round(triang,6),',Quadrangle =',rect,'"')