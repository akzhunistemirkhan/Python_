import os
from random import randint
with open('my.txt', 'r', encoding='utf-8') as f:
    l = f.readlines()
with open('your.txt', 'r', encoding='utf=8') as f1:
    l1 = f1.readlines()
n = int(input())
for i in l:
    print(i + ' ' + l1[n])