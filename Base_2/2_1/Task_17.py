word = input()
word = word.lower()
word = word.split()
word = ''.join(word)
rev = list(word)
word = list(word)
rev.reverse()
if word == rev:
    print('YES')
else:
    print('NO')