import re
n = int(input())
for i in range(n):
    a = input().strip()
    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", a) and not re.search(r"([\d])\1\1\1", a.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")

