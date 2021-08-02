
def star(r, c, size):
    if size == 1:
        arr[r][c] = '*'

    else:
        n_size = size // 3
        star(r, c, n_size)
        star(r, c + n_size, n_size)
        star(r, c + n_size * 2, n_size)

        star(r + n_size, c, n_size)
        star(r + n_size, c + n_size * 2, n_size)

        star(r + n_size * 2, c, n_size)
        star(r + n_size * 2, c + n_size, n_size)
        star(r + n_size * 2, c + n_size * 2, n_size)


N = int(input())
arr = [[' '] * N for _ in range(N)]

star(0, 0, N)
for i in range(N):
    print(''.join(arr[i]))
    ## 왜 print(*arr[i]) 는 좀 다르게 나오지?? 알슈가 없네~~



