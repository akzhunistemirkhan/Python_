#15
def sort(a):
    a.sort()
    print(*a,sep="-")
a = input().split("-")   
sort(a)