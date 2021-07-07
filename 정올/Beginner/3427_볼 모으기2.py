
N = int(input())
balls = list(input())

def move_ball(color, min_cnt):

    diff_color_idx_a = N
    diff_color_idx_b = N
    cnt_a = 0
    cnt_b = 0

    for i in range(N-1, -1, -1):
        if balls[i] != color:
            diff_color_idx_a = i
            break

    for i in range(N):
        if balls[i] != color:
            diff_color_idx_b = i
            break

    for i in range(diff_color_idx_a - 1, -1, -1):
        if balls[i] == color:
            cnt_a += 1

            if cnt_a >= min_cnt:
                return min_cnt

    min_cnt = cnt_a

    for j in range(diff_color_idx_b + 1, N):
        if balls[j] == color:
            cnt_b += 1

            if cnt_b >= min_cnt:
                return min_cnt
    # print('지금 color : ', color, 'cnt_a :', cnt_a, "cnt_b :", cnt_b )
    if cnt_a < cnt_b:
        return cnt_a

    return cnt_b


cnt_r = move_ball('R', N)
cnt_b = move_ball('B', cnt_r)

res = cnt_r
if cnt_b < cnt_r:
    res = cnt_b

print(res)
