dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def power(r, c, col):
    global cnt
    arr[r][c] = -1
    cnt += 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N:
            if arr[nr][nc] == col:
                power(nr, nc, col)


N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]

w_res, b_res = 0, 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 'W':
            cnt = 0
            power(i, j, 'W')
            w_res += cnt**2
        elif arr[i][j] == 'B':
            cnt = 0
            power(i, j, 'B')
            b_res += cnt**2

print(w_res, b_res)

