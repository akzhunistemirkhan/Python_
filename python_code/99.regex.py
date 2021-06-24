import re
mytext = input()
textlookfor = r"[A-z]+[a-z]+$"
if re.search(textlookfor, mytext):
    print('Found a match!')
else:
    print('Not matched!')
