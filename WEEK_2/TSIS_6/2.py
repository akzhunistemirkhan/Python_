def function(n):
    ans = 0
    for i in n:
        ans += i
    return ans
n = list(map(int,input().split()))    
print(function(n))