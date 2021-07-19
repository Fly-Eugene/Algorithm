
def check(d):
    # print('=================================')
    # print('현재 측정거리는', d)
    wifi_cnt = 1
    prev = houses[0]
    res = 1000000000

    for h_idx in range(1, N):
        if houses[h_idx] - prev >= d:
            res = min(res, houses[h_idx] - prev)
            wifi_cnt += 1
            # print('현재 wifi 설치개수', wifi_cnt)
            # print('houses[h_idx] :', houses[h_idx], 'prev :', prev)
            prev = houses[h_idx]

        if wifi_cnt == C:
            break


    if wifi_cnt < C:
        # print('와이파이 개수 못채움!!')
        return False

    # print('성공!! 결과는', res)
    return res

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

min_dis = houses[0]
for idx in range(1, N):
    min_dis = min(min_dis, houses[idx]-houses[idx-1])


max_dis = houses[-1]

ans = 0
while min_dis <= max_dis:
    mid = (min_dis + max_dis) // 2
    if check(mid):
        ans = max(ans, check(mid))
        min_dis = mid + 1
    else:
        max_dis = mid - 1

print(ans)