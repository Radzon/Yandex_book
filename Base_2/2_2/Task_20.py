s_1 = str(input())
s_2 = str(input())
s_3 = str(input())
max_s = max(s_1, s_2, s_3)
min_s = min(s_1, s_2, s_3)
if (s_1 < s_2 < s_3) or (s_1 > s_2 > s_3):
    sr = s_2
elif (s_2 < s_1 < s_3) or (s_2 > s_1 > s_3):
    sr = s_1
else:
    sr = s_3
if 'зайка' in min_s:
    print(min_s, len(min_s))
elif 'зайка' in sr:
    print(sr, len(sr))
else:
    print(max_s, len(max_s))