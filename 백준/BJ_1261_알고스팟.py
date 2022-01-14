from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):

    queue = deque()
    queue.append((r, c, 0))
    visited[r][c] = 0

    while queue:
        cr, cc, cd = queue.popleft()
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == -1:
                    if arr[nr][nc] == 0:
                        visited[nr][nc] = cd
                        queue.append((nr, nc, cd))
                    elif arr[nr][nc] == 1:
                        visited[nr][nc] = cd + 1
                        queue.append((nr, nc, cd + 1))
                else:
                    if arr[nr][nc] == 0 and cd < visited[nr][nc]:
                        visited[nr][nc] = cd
                        queue.append((nr, nc, cd))

                    elif arr[nr][nc] == 1 and cd + 1 < visited[nr][nc]:
                        visited[nr][nc] = cd + 1
                        queue.append((nr, nc, cd + 1))


M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

bfs(0, 0)

print(visited[N-1][M-1])



