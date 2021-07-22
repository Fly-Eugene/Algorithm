def check1(high):
    left, right = 0, len(not_reverse) - 1
    res = -1

    while left <= right:
        mid = (left + right) // 2
        if not_reverse[mid] < high:
            res = max(res, mid)
            left = mid + 1
        else:
            right = mid - 1

    if res == -1:
        return len(not_reverse)

    return len(not_reverse) - (res + 1)

def check2(high):
    global H

    left, right = 0, len(reverse) - 1
    res = len(reverse)

    while left <= right:
        mid = (left + right) // 2

        if H - reverse[mid] >= high:
            right = mid - 1
            res = min(res, mid)

        else:
            left = mid + 1

    return res


N, H = map(int, input().split())

not_reverse = []
reverse = []

for i in range(N):
    if i % 2 == 0:
        not_reverse.append(int(input()))

    else:
        reverse.append(int(input()))

reverse.sort(reverse=True)
not_reverse.sort()


cnt = 0
obstacle_cnt = N

for i in range(1, H+1):
    temp = check1(i) + check2(i)

    if temp < obstacle_cnt:
        cnt = 1
        obstacle_cnt = temp
    elif temp == obstacle_cnt:
        cnt += 1
    else:
        continue

print(obstacle_cnt, cnt)



