def function(s):
    up, low = 0, 0
    for i in s:
        if i.islower(): 
            low += 1
        elif i.isupper(): 
            up += 1
    print('Upper case:', up)
    print('Lower case:', low)
function(input())