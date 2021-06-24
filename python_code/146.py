n = int(input())
a = list(map(int,input().split()))
maxi = a[0]
mini = a[0]
for i in range(len(a)):
    if a[i] > maxi:
        maxi = a[i]
    if a[i] < mini:
        mini = a[i]
maxi,mini = mini,maxi   
print(a)
  
    