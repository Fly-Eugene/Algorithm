dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    global cnt
    arr[r][c] = 1
    cnt += 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N:
            if arr[nr][nc] == 0:
                dfs(nr, nc)
    return


M, N, K = map(int, input().split())
point_list = [list(map(int, input().split())) for _ in range(K)]

arr = [[0] * (N) for _ in range(M)]

for i in range(K):
    c1, r1, c2, r2 = point_list[i]
    for r in range(r1, r2):
        for c in range(c1, c2):
            arr[r][c] = 1

res = []

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            cnt = 0
            dfs(i, j)
            res.append(cnt)

print(len(res))
print(*sorted(res))


