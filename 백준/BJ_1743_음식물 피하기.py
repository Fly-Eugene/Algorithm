
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    global res

    stack = [(r, c)]
    visited[r][c] = 1
    tmp = 1

    while stack:
        r, c = stack.pop()

        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == 0 and arr[nr][nc] == 1:
                    stack.append((nr, nc))
                    visited[nr][nc] = 1
                    tmp += 1

    if res < tmp:
        res = tmp

N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

res = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)

print(res)