

A = [1, 1, 3, 4, 4, 4]
cnt_list = [0] * (A[-1] + 1)

for a in A:
    cnt_list[a] += 1

res = 0
for i in range(1, len(cnt_list)):
    if cnt_list[i] == 0:
        continue

    if cnt_list[i] < i:
        half = i // 2
        if cnt_list[i] <= half:
            res += cnt_list[i]

        else:
            res += (i - cnt_list[i])

    elif cnt_list[i] > i:
        res += (cnt_list[i] - i)

print(cnt_list)
print(res)
