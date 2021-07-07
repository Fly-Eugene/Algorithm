

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


def M2(idx):
    if idx == N:
        if tuple(dice_cnt) in duple_set:
            return
        else:
            print(*sel)
            duple_set.add(tuple(dice_cnt))
            return

    if check[idx] == 0:
        for j in range(1, 7):
            sel[idx] = j
            dice_cnt[j] += 1
            check[idx] = 1

            M2(idx + 1)
            check[idx] = 0
            dice_cnt[j] -= 1

def M3(idx):

    if idx == N:
        print(*sel)
        return


    if check[idx] == 0:
        for j in range(1, 7):
            if dice_cnt[j] == 0:
                dice_cnt[j] += 1
                check[idx] = 1
                sel[idx] = j
                M3(idx+1)

                dice_cnt[j] -= 1
                check[idx] = 0




N, M = map(int, input().split())
sel = [0] * N
check = [0] * N
dice_cnt = [0] * 7
duple_set = set()

if M == 1:
    M1(0)
elif M == 2:
    M2(0)
else:
    M3(0)



