file = open("my.txt")
line_count = 0
for linei in file:
    line_count += 1
if line_count == 0:
    print('No')
else:
    print('Good')
    print(line_count)