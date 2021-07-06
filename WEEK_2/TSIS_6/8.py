ans = list()
def function(list):
    for i in list:
        if i not in ans: ans.append(i) 
        return ans
list = list(map(int, input().split()))
print(function(list))