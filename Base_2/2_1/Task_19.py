s = [x for x in input().split()]
stack = []
for x in s:
    if x in '*+-':
        b = stack.pop()
        a = stack.pop()
        stack.append(eval(f'{a} {x} {b}'))
    else:
        stack.append(x)
print(stack[0])