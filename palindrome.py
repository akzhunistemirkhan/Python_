# aba - ok
# acbbca - ok
# abc - not
# abbaa - not
line = input()
ok = True
for i in range(len(line) // 2):
  # print(line[0], line[len(line) - 0 - 1])
  # print(line[1], line[len(line) - 1 - 1])
  # print(line[2], line[len(line) - 2 - 1])
  
  # print(line[i], line[len(line) - i - 1])
  if line[i] != line[len(line) - i - 1]:
    ok = False
    break
if ok:
  print('YES')
else:
  print('NO')

#2
line = input()
# if line == line[::-1]:
#   print('YES')
# else:
#   print('NO')

# print('YES') if line == line[::-1] else print('NO')
print('YES') if line == ''.join(reversed(line)) else print('NO')

