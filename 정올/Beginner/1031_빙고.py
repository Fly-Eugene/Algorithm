def bingo_row(i):
    cnt = 0
    for j in range(5):
        if bingo_arr[i][j] == 0:
            cnt += 1
    if cnt == 5:
        return 1
    return 0

def bingo_col(j):
    cnt = 0
    for i in range(5):
        if bingo_arr[i][j] == 0:
            cnt += 1
    if cnt == 5:
        return 1
    return 0

def bingo_cross_1():
    cnt_a = 0
    for i in range(5):
        if bingo_arr[i][i] == 0:
            cnt_a += 1

    if cnt_a == 5:
        return 1
    return 0

def bingo_cross_2():
    cnt_b = 0
    for i in range(5):
        if bingo_arr[i][4-i] == 0:
            cnt_b += 1

    if cnt_b == 5:
        return 1
    return 0

bingo_arr = [list(map(int, input().split())) for _ in range(5)]
order = []
for _ in range(5):
    order.extend(list(map(int, input().split())))


res_row, res_col, res_cross_1, res_cross_2 = 0, 0, 0, 0
bingo_cnt = 0
stop = 1
for idx in range(len(order)):
    for i in range(5):
        for j in range(5):
            if bingo_arr[i][j] == order[idx]:
                bingo_arr[i][j] = 0
                res_row = bingo_row(i)
                res_col = bingo_col(j)
                if i == j:
                    res_cross_1 = bingo_cross_1()
                if i == 4 - j:
                    res_cross_2 = bingo_cross_2()
                break
        if res_row:
            bingo_cnt += 1
            res_row = 0
        if res_col:
            bingo_cnt += 1
            res_col = 0
        if res_cross_1:
            bingo_cnt += 1
            res_cross_1 = 0
        if res_cross_2:
            bingo_cnt += 1
            res_cross_2 = 0

    # print('-----------------')
    # for r in range(5):
    #     print(bingo_arr[r])
    # print('빙고 개수는', bingo_cnt)

    if bingo_cnt >= 3:
        print(idx+1)
        stop = 1
        break
