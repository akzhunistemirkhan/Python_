def maskify(s) :
    return '#' * (len(s) - 4) + s[-4:]

alpha = 'abcdefghij'
data = [alpha[:i] for i in range(len(alpha)+1)]

for s in data:
    print((s, maskify(s)))