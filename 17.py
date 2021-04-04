#количество положительных 1 -2 3 -4 5 => 3
def main():
    print(sum(int(i) > 0 for i in  input().split()))
 
main()
