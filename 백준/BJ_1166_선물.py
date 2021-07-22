
N, L, M, H = map(int, input().split())

min_len = 1
max_len = max(L, M, H)
res = 0


for _ in range(60):
    mid = (min_len + max_len) / 2
    cnt = (M//mid) * (H//mid) * (L//mid)

    # if max_len < min_len:
    #     min_len, max_len = max_len, min_len

    if cnt >= N:
        res = max(mid, res)
        min_len = mid + 1

    else:
        max_len = mid - 1

print(float(round(res, 9)))

