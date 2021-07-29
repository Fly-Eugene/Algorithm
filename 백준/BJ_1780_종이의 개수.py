def check(r, c, size):
    global minus_cnt, zero_cnt, plus_cnt
    now = arr[r][c]

    for i in range(r, r+size):
        for j in range(c, c+size):
            if arr[i][j] != now:
                n_size = size // 3
                check(r, c, n_size)
                check(r, c + n_size, n_size)
                check(r, c + n_size * 2, n_size)

                check(r + n_size, c, n_size)
                check(r + n_size, c + n_size, n_size)
                check(r + n_size, c + n_size * 2, n_size)

                check(r + n_size * 2, c, n_size)
                check(r + n_size * 2, c + n_size, n_size)
                check(r + n_size * 2, c + n_size * 2, n_size)

                return

    if now == -1:
        minus_cnt += 1
        return

    elif now == 1:
        plus_cnt += 1
        return

    else:
        zero_cnt += 1
        return



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

minus_cnt = 0
zero_cnt = 0
plus_cnt = 0

check(0, 0, N)

print(minus_cnt)
print(zero_cnt)
print(plus_cnt)
