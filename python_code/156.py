input = open('input.txt','r')
output = open('output.txt','w')
file = input.read().split('\n')
a = list()
text = input.readlines()
print(text)
for i in file:
    a.append(len(i))
for i in range(1,len(a)):
    print(a[i],a[i-1])
    if a[i] == a[i-1]:
        print("No",file = output,end="")
        exit()
print("Yes",file = output,end="")     
