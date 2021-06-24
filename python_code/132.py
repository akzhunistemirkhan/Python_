def pascal(a):  
    for i in range(1,a+1):  
        b=1
        for j in range(1,i+1):  
            print(b,end=" ")  
            b = int(b*(i-j)/j)
        print("")
a = int(input())
pascal(a)