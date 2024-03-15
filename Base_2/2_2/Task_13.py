elf = int(input())
gnom = int(input())
human = int(input())
fist_e = elf // 10
last_e = elf % 10
fist_g = gnom // 10
last_g = gnom % 10
fist_h = human // 10
last_h = human % 10
if fist_h == fist_e == fist_g:
    print(fist_h)
else:
    print(last_h)