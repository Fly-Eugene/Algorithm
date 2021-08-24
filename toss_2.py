
def check(seconds, cnt, idx):
    global min_cnt

    if seconds == 0:
        if cnt < min_cnt:
            min_cnt = cnt
        return

    if idx > 3 or seconds < 0:
        return

    if eating_seconds[idx] <= seconds:
        max_cnt = seconds // eating_seconds[idx]

        for i in range(max_cnt + 1):
            if i <= snack_cnt[idx]:
                check(seconds - eating_seconds[idx] * i, cnt + i, idx + 1)

    else:
        check(seconds, cnt, idx + 1)


eating_seconds = [300, 130, 120, 20]
snack_cnt = [10, 30, 20, 30]

seconds = 460
min_cnt = 10000000000

check(seconds, 0, 0)

if min_cnt == 10000000000:
    print(0)
else:
    print(min_cnt)



