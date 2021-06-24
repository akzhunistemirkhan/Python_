s = input()
word = ''
maxLen = 0
maxWord = ''
for c in s+' ':
    if c == ' ':
        if len(word) > maxLen:
            maxWord = word
        word = ''
    else:
        word += c


print(maxWord)
print(len(maxWord))