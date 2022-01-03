dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    global cnt

    queue = [(r, c)]
    arr[r][c] = -1
    cnt += 1

    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1:
                    queue.append((nr, nc))
                    arr[nr][nc] = -1

T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * (M) for _ in range(N)]
    cnt = 0

    for _ in range(K):
        b, a = map(int, input().split())
        arr[a][b] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i, j)

    print(cnt)
