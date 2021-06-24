def case(s):
    num = 0
    mum = 0
    for i in s:
        if i.isupper():
            num += 1
        return num    
        if i.islower():
            mum += 1
        return mum        
s = map(str,input().split())
print(case(s))    

#'''''s = input()
cntu=0
cntl=0
for i in s:
    if i.isupper():
        cntu+=1
    if i.islower():
        cntl+=1
print("No. of Upper case characters :",cntu)
print("No. of Lower case Characters :",cntl)


