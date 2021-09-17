#Hello            me
#it's      =>     it's
#me               Hello

a,b,c=input(),input(),input()
print(c)
print(b)
print(a)

[print(i) for i in [input() for _ in range(3)][::-1]]

print(*reversed([input(), input(), input()]), sep="\n")

a, b, c =[input() for _ in range(3)]
print(c,b,a, sep="\n")

print("{2}\n{1}\n{0}\n".format(input(), input(), input()))

