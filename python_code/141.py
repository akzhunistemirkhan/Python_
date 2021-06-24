import collections
file = open("my.txt")
print(*collections.Counter(file))