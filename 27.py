#1 =>    1 + 1 = 2
#        1 + 2 = 3
#        1 + 3 = 4
#        1 + 4 = 5
#        1 + 5 = 6
#        1 + 6 = 7
#        1 + 7 = 8
#        1 + 8 = 9
#        1 + 9 = 10
n = int(input())
for i in range(1,n+1):
    for j in range(1,10):
        print(i,'+',j,'=',i+j)
    print()    
