import re
p = r'\w+ (<[a-zA-Z]{1}[\w._-]+?@[a-z]+.[a-z]{1,3}>)'
for i in range(int(input())):
    a = input()
    if re.search(p, a):
        print(a)