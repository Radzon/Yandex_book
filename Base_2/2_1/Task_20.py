s = [x for x in input().split()]
stack = []
for x in s:
    if x in '*+-/':
        b = stack.pop()
        a = stack.pop()
        if x == '/':
            x = '//'
        stack.append(eval(f'{a} {x} {b}'))
    elif x in '~!#':
        if x == '~':
            stack.append(f'-{stack.pop()}')
        if x == '#':
            stack.append(a := stack.pop())
            stack.append(a)
        if x == '!':
            a = int(stack.pop())
            res = 1
            for i in range(1, a + 1):
                res *= i
            stack.append(str(res))
    elif x in '@':
        stack.append(stack.pop(-3))
    else:
        stack.append(x)
print(*stack)