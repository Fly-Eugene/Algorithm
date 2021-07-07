
def dice_sum(idx, res):
    if idx == N:
        if res == M:
            print(*sel)
        return

    if check[idx] == 0:
        for i in range(1, 7):
            sel[idx] = i
            check[idx] = 1
            res += i
            dice_sum(idx+1, res)

            res -= i
            check[idx] = 0


N, M = map(int, input().split())
sel = [0] * N
check = [0] * N

dice_sum(0, 0)