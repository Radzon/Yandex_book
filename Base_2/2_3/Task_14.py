numb = int(input())
root = (numb ** 0.5)
s = 2
prime = 'YES'
if numb == 1:
    prime = 'NO'
else:
    for i in range(int(root)):
        if (numb / s) % 1 == 0:
            prime = 'NO'
        else:
            pass
        s += 1
print(prime)