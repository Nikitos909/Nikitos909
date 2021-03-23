from math import sqrt
a = input('input your positive number:103\n')
if a.isdigit() == False or int(a) <= 0:
    print('Incorrect input, please try again later')
else:
    a = int(a)
    l = []
    for i in range(2, int(sqrt(a)) + 1):
        if a % i == 0:
            l.append(i)
    if sum(l) > 0:
        print(f'{a} - The number is complex')
    else:
        print(f'{a} - The number is prime')