import re
txt = "The rain in Spain 1234"
x = re.search(r"(.+)(\b[0-9]+)",txt)
print(*x.groups())
print(x.group(1))
print(x.group(2))