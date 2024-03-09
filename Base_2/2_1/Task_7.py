numb = input()
out = 0
numb = numb.split()
for i in range(len(numb)):
    out += int(numb[i])
print(out)