def first_line(name, n):
        from itertools import islice
        with open(name) as a:
                for line in islice(a, n):
                        print(line)
                       
first_line('my.txt',7)