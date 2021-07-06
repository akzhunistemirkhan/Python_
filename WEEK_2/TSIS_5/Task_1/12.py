file = open("my.txt",'w')
s = ''
text = [word for word in input()]
for i in text:
    s += i
file.write(s)