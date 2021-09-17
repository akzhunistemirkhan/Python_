a = input()
b,c,d = input(),input(),input()       
print(b,c,d, sep = a)
# *
# Раз
# Два        Раз*Два*Три  
# Три

s=input()
print(input(),input(),input(), sep = s)

print(input().join([input() for _ in range(3)]))

a,b,c,d = [input() for _ in range(4)]
print(b,c,d, sep = a)