
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, crashed):
    queue = deque()
    queue.append((r, c, crashed))
    visited[r][c][crashed] = 1

    while queue:
        c_r, c_c, c_crashed = queue.popleft()
        if c_r == N-1 and c_c == M-1:
            return visited[N-1][M-1][c_crashed]
        for i in range(4):
            nr, nc = c_r+dr[i], c_c+dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                # 벽 안부수기
                if arr[nr][nc] == 0 and visited[nr][nc][c_crashed] == 0:  # 갈 곳이 통로이고, 간 적이 없으면
                    queue.append((nr, nc, c_crashed))
                    visited[nr][nc][c_crashed] = visited[c_r][c_c][c_crashed] + 1
                elif arr[nr][nc] == 1 and c_crashed == 0:  # 주변이 벽이고 아직 벽을 깬 적이 없으면
                    queue.append((nr, nc, c_crashed + 1))
                    visited[nr][nc][c_crashed + 1] = visited[c_r][c_c][c_crashed] + 1

    return -1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

print(bfs(0, 0, 0))