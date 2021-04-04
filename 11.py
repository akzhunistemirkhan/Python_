#PRINT->
#"Python is a great language!", said Fred. "I don't ever remember having this much fun before."
#1
print('"Python is a great language!", said Fred.',end = ' ')
print('"I don'"'t ever remember having",'this much fun before."')
#2
print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')
#3
print('"Python is a great language!", said Fred. "I don\'t ever remember having this much fun before."')
#4
print('"Python is a great language!", said Fred. "' + 'I ' + "don't " + 'ever remember having this much fun before."')
#5
s1 = '"Python is a great language!", said Fred. "I don'
s2 = "'t ever remember having this much fun before."
s3 = '"'
print(s1 + s2 + s3)
