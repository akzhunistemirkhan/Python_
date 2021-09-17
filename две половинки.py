#abcdef => defabc     #abcdefg => efgabcd
a = input()
b=len(a)//2
c = len(a)%2
d = b+c
print(a[d:]+a[0:d],end='')

#2
s = input()
print(s[-(len(s)//-2):]+s[:-(len(s)//-2)])

#3
from math import *
s = input()
i = ceil(len(s)/2)
print(s[i:]+s[:i])