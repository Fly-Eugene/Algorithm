
str_list = input()
res = 10

for idx in range(1, len(str_list)):
    if str_list[idx-1] == str_list[idx]:
        res += 5
    else:
        res += 10

print(res)

