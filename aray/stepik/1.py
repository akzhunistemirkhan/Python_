for i in range(1,8):
    for j in range(i):
        print('*', end='')
    print()
# *
# **                        for i in range(8):       c = '*'
# ***                           print('*'*i)         for i in range(1, 8):
# ****                                                  print(i*c)
# *****
# ******
# *******