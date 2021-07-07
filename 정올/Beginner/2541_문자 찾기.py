
str_list = input()

koi_cnt = 0
ioi_cnt = 0

idx = 0
while idx < len(str_list):
    if str_list[idx:idx+3] == 'KOI':
        koi_cnt += 1
        idx += 2
    elif str_list[idx:idx+3] == 'IOI':
        ioi_cnt +=1
        idx += 2
    else:
        idx += 1

print(koi_cnt)
print(ioi_cnt)
