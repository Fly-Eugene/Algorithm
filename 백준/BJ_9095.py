

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [[0] * (N+1) for _ in range(N)]
    if N <= 3:
        for i in range(N):
            arr[0][i+1] = 1
    else:
        arr[0][1], arr[0][2], arr[0][3] = 1, 1, 1

    res = 0

    for i in range(N-1):
        for j in range(1, N+1):
            if arr[i][j] != 0:
                for n in range(1, 4):
                    n_num = j + n
                    if 0 <= n_num < N + 1:
                        arr[i+1][n_num] += arr[i][j]

        res += arr[i][N]
    res += arr[N-1][N]

    print(res)
