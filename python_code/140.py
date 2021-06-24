#count the number of lines in a text file.
file = open("my.txt")
count = 0
for i in file:
    count += 1
print(count)