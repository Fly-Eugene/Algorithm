from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    global day, cnt, ripe

    while ripe:
        r, c, d = ripe.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0:
                    ripe.append((nr, nc, d+1))
                    arr[nr][nc] = 1
                    cnt += 1
                    if day < d+1:
                        day = d+1


M, N = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

ripe = deque()
day = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            ripe.append((i, j, 0))
            cnt += 1
        elif arr[i][j] == -1:
            cnt += 1

if ripe == []:
    print(0)
else:
    bfs()
    if cnt == N*M:
        print(day)
    else:
        print(-1)

