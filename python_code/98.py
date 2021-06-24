#Дан файл инпута, надо считать строки и вывести йес, если каждая послед строка
#  длиннее предыдущей, иначе ноу, и вывод в файл аутпута сделать

a = list(map(str,input().split()))
ok = True
for i in range(1,len(a)):
    if len(a[i-1]) > len(a[i]):
        ok = False
        break
if ok:
    print("Yes")
else: 
    print("NO")    