
def M1(idx):
    if idx == N:
        print(*sel)
        return

    if check[idx] == 0:
        for j in range(1, 7):
            sel[idx] = j
            check[idx] = 1
            M1(idx + 1)

            check[idx] = 0



N, M = map(int, input().split())
sel = [0] * N
check = [0] * N
dice_cnt = [0] * 7
duple_set = set()

if M == 1:
    M1(0)



