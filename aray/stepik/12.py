# 10                 1 10.0
#  50       =>       2 15.0
# 6                  3 22.5
#                    4 33.75
#                    5 50.625
#                    6 75.9375
a,b,c = int(input()),int(input()),int(input())
print('1',float(a))
for i in range(c-1):
    a = a+a*b/100
    print(i+2,a)