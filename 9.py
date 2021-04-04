a = input().split()
count = 0
for i in a:
    if len(i) > count:
        count = len(i)
        word = i    
print(word)
print(len(word))
#самое длинное слово
