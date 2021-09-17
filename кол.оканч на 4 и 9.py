a=int(input())
b=int(input())
count=0
for i in range(a,b+1):             # => 1 
    if (i**3)%10==4:               #    10  => 2
        count += 1
    if (i**3)%10==9:
        count += 1
print(count)         
