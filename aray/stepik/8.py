#самое короткое и самое длинное название города
city1, city2, city3 = input(), input(), input()
len1, len2, len3 = len(city1), len(city2), len(city3)
m = max(len1, len2, len3)
n = min(len1, len2, len3)
if n == len1:
    print(city1)
if n == len2:
    print(city2)
if n == len3:
    print(city3)
if m == len1:
    print(city1)
if m == len2:
    print(city2)
if m == len3:
    print(city3)

#2
a = input()
b = input()
c = input()
print(min (a, b, c, key=len))
print(max (a, b, c,  key=len))

#3
a, b, c = [input() for _ in range(3)]
print(min(a, b, c, key=len))
print(max(a, b, c, key=len))

