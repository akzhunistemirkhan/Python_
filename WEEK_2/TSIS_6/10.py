def function(s):
    for i in s:
        if i%2 == 0:
            print(i, end=' ')
s = list(map(int, input().split()))
function(s)