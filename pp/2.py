n = int(input())
if n % 2 != 0:
    print("Super")
if n%2==0 and n in range(2,5):
    print("Not super")
if n%2==0 and n in range(6,20):
    print("Super")
if n%2==0 and n in range(20,101):
    print("Not super")