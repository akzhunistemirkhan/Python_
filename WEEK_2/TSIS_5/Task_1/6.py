s = ''
with open(r'my.txt','r') as f:
    for text in f:
        if text != '\n':
            s+=text
    print(s)