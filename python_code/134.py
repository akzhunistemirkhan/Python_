import os
def file_text(name):
        txt = open(name)
        print(txt.read())
file_text('my.txt')