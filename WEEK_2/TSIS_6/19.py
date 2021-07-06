def func(a):
    def function1(b):
        nonlocal a
        a += 1
        return a+b**2
    return function1
a = func(4)
print(a(4))