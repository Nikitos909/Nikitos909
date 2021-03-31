def check_brackets(formula: str, brackets: str):
    list_f = [x for x in formula]
    list_b = [x for x in brackets]
    stack = []

    def add_brackets(l):
        l_add = []
        for i in l:
            if i == '(':
                l_add.append(')')
            elif i == '[':
                l_add.append(']')
            elif i == '{':
                l_add.append('}')
            elif i == '<':
                l_add.append('>')
            elif i == ')':
                l_add.append('(')
            elif i == ']':
                l_add.append('[')
            elif i == '}':
                l_add.append('{')
            elif i == '>':
                l_add.append('<')
        return l_add

    a = []
    b = []
    for i in range(len(list_f)):
        if list_f[i] in list_b:
            stack.append(list_f[i])

        elif list_f[i] in add_brackets(list_b):
            if add_brackets(list_f[i]) == [stack[-1]]:
                stack.pop()
            else:
                a.append(list_f[i])
                b.append(i)
                for j, e in reversed(list(enumerate(list_f))):
                    if j > b[0]:
                        continue
                    elif j < b[0] and e == stack[-1]:
                        b.append(j)
                break

    if stack:
        print(f'False, {(a[0], b[0])}, {(stack[-1], b[1])}')
    else:
        print(f'True, None, None')

check_brackets('(a+[b*c]-17)', '([')

