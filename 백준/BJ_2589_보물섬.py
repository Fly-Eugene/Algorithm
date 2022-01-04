from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, dis, visited):
    global max_dis, N, M

    queue = deque()
    queue.append((r, c, dis))
    visited[r][c] = 1

    while queue:
        r, c, dis = queue.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 'L' and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    queue.append((nr, nc, dis + 1))
                    if max_dis < dis + 1:
                        max_dis = dis + 1

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input()))

max_dis = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            visited = [[0] * M for _ in range(N)]
            dfs(i, j, 0, visited)

print(max_dis)
