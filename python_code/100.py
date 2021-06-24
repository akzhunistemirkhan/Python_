import re
mytext = input()
textlookfor = r"[A-Z]+[a-z]+"
if re.search(textlookfor, mytext):
    print('Yes')
else:
    print('No')