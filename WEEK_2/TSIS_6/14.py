def pangram(s):
    a = set()
    for i in s:
        if i == ' ': 
            continue
        else: 
            a.add(i.lower())
    return len(a) == 26
print(pangram(input()))