import re
f = open("my.txt").readlines()
print([words.rstrip('\n')for words in f])

