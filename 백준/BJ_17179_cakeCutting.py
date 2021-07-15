
def cake_cutting(length, q):

    shortest = 4000001       # 가장 길이가 짧은 케이크의 길이를 찾을 것이다
    prev_length = 0           # 이전에 짜른 케이크 길이
    now_idx = 0

    while q > 0 and now_idx < M:
        if cuttings[now_idx] - prev_length >= length:
            shortest = min(shortest, cuttings[now_idx] - prev_length)
            prev_length = cuttings[now_idx]
            q -= 1

        now_idx += 1

    if q == 0 and (L - prev_length) >= length:
        return min(shortest, L - prev_length)

    return False




N, M, L = map(int, input().split())
cuttings = [int(input()) for _ in range(M)]

for tc in range(N):
    q = int(input())

    min_len = min(cuttings[0], L - cuttings[-1])

    for idx in range(M-1):
        min_len = min(min_len, cuttings[idx+1] - cuttings[idx])




    l = min_len
    r = L
    res = 0

    while l <= r:
        mid = (l+r) // 2
        if cake_cutting(mid, q):
            res = max(res, cake_cutting(mid, q))
            l = mid + 1

        else:
            r = mid - 1


    print(res)
