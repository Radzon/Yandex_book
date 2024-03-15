total = int(input())
name = input()
for i in range(total - 1):
    name = min(name, input())
print(name)