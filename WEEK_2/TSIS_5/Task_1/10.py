file = open(r'my.txt','r')
str = file.read().split(' ')
file.close()
a = {word:0 for word in str}
print(a)
for word in str:
    a[word]+=1
for key,value in a.items():
    print(key,value)