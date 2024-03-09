dlina = int(input())
n = int(input())
for i in range(n):
    string = (input())[:dlina + 1]
    if len(string) > dlina:
        string = (string[:(dlina - 3)] + '...')
    print(string)