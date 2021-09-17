import re
str = input()
string = r"^^PP2.*midterm$"
if re.match(string, str,re.IGNORECASE):
    print("Success")
else:
    print("No")