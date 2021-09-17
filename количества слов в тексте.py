#In 2010, someone paid 10k Bitcoin for two pizzas. => 9
s = input()
print(s.count (" ") + 1)

#2
print(input().strip().count(' ') + 1)

#3
s, total = input(), 0
s = s.strip()
for i in range(len(s)):
    if s[i] == ' ':
        total += 1
print(total + 1)

#4
s = input()
print(len(s.split()))

#5
words = input()
count = 0
for word in words:
    if word == ' ':
        count += 1
print(count + 1)

