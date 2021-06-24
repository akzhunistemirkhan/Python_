import re

file = open('raw1.txt','r',encoding='utf-8')
text = file.read()

#filialpatter = r"\nФилиал.*"
#x = re.search(filialpatter,text)
#print(x)   => span=(8,37), match='\nФилиал ТОО EUROPHARMA Астана'>

binpatter = r"\nБИН.*(?p<BIN>\b[0-9]+)"
x = re.search(binpatter,text)
print(x.group("BIN"))


file.close()