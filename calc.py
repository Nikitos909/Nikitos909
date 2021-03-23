a = input('Input your first number:\n')
while True:
    if a.isdigit():
        a = float(a)
        break
    else:
        a = input('Your input is incorrect, please try again:\n')
b = input('Input math operation(+,-,*,/,**) and second number separated by a space:\n')
while True:
    if len(b.split()) == 2:
        oper, num = b.split()[0], b.split()[1]
        if oper == '+':
            a += float(num)
            b = input()
        elif oper == '-':
            a -= float(num)
            b = input()
        elif oper == '*':
            a *= float(num)
            b = input()
        elif oper == '/':
            if float(num) == 0:
                b = input('Division by zero impossible, try again:\n')
            else:
                a /= float(num)
                b = input()
        elif oper == '**':
            a **= float(num)
            b = input()
    else:
        if b.split()[0] == '=':
            print(a)
            break
        else:
            b = input('Your input is incorrect, try again:\n')