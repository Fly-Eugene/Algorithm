
# 비어있는 곳 : ., 물 : * , 돌 : X, 비버의 굴 : D, 고슴도치의 위치 : S

## 고숨도치 이동, 물도 계속 확장
# 고슴도치는 물과 돌을 지나갈 수 없다.
# 고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다 ? => 물을 먼저 채우고 고슴도치 이동시키기

from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def water(): ## 현재 물이 차있는 4방면으로 한칸씩 확장한다.
    global N, M

    queue = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == "*":
                queue.append((i, j))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] != "D" and arr[nr][nc] != "X":
                    arr[nr][nc] = "*"

def s_move(i, j):

    water()
    depth = 1

    queue = deque()
    queue.append((i, j, 0))
    visited = [[0] * M for _ in range(N)]

    while queue:
        r, c, dis = queue.popleft()
        if depth == dis:   ## 거리가 멀어지는 순간, 홍수의 확장을 진행
            depth += 1
            water()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if arr[nr][nc] == "D":
                    return dis + 1
                elif arr[nr][nc] == ".":
                    queue.append((nr, nc, dis + 1))
                    visited[nr][nc] = 1

    return "KAKTUS"



N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

sr, sc = 0, 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S':
            sr, sc = i, j

res = s_move(sr, sc)
print(res)
