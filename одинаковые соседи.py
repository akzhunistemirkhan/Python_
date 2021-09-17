a = input()
sum = 0
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        sum += 1
print(sum)

# aabbcc  => 3

#2
s = input()
f = 0
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        f += 1
print(f)