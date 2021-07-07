def move_ball(color, min_cnt):

    cnt = 0
    diff_color_idx = N

    # 다른 컬러 마지막 인덱스 찾기 => 그 뒤로 쌓을 거니까
    for i in range(N-1, -1, -1):
        if balls[i] != color:
            diff_color_idx = i
            break

    if diff_color_idx == N:
        return 0

    while True:
        print(balls, '현재 cnt : ', cnt)
        idx = -1
        # 다른 컬러 마지막부터 앞쪽으로 원하는 컬러 찾기
        for i in range(diff_color_idx - 1, -1, -1):
            if balls[i] == color:
                idx = i
                break

        if idx == -1:
            break
        else:
            balls.pop(idx)
            balls.append(color)
            cnt += 1
            diff_color_idx -= 1

        if min_cnt <= cnt:
            return N

    return cnt


N = int(input())
balls = list(input())
cnt_r = move_ball('R', N)
cnt_b = move_ball('B', cnt_r)

res = cnt_b
if cnt_r < cnt_b:
    res = cnt_r

print(res)