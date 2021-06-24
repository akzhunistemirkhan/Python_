import re 
mytext = input()
textlookfor = r"\d\d\d\d"
allresults = re.findall(textlookfor, mytext)
print(*allresults)

