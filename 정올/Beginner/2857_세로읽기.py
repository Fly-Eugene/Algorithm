
str_list = []
max_len = 0
for _ in range(5):
    item = input()
    if max_len < len(item):
        max_len = len(item)
    str_list.append(item)

idx = 0
res = ''
while idx < max_len:

    for item in str_list:
        if idx < len(item):
            res += item[idx]
        else:
            continue

    idx += 1

print(res)
