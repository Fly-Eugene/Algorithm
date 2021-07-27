
N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]
times.sort()

## 이분탐색이라고 무조건 정렬된 무언가가 필요한 것은 아니다
min_time = 0
max_time = max(times) * M
res = max_time

while min_time <= max_time:
    mid = (min_time + max_time) // 2
    people = 0

    for time in times:
        people += mid // time
        if people >= M:
            break

    if people >= M:
        max_time = mid - 1
        res = mid

    else:
        min_time = mid + 1

print(res)


