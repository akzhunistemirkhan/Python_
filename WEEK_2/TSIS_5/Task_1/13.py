file = open("my.txt")
ok = open("your.txt","w")
for lines in file:
    ok.write(lines)