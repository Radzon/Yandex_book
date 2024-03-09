numb = input()
numb = numb.split()
q = int(input())
for i in range(len(numb)):
    print(int(numb[i]) ** q, end=' ')