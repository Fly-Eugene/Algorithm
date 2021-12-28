
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, 1, -1]

def bfs(sharks):
    global res

    queue = sharks
    while queue:
        r, c, d = queue.pop(0)
        for i in range(8):
            nr, nc, nd = r+dr[i], c+dc[i], d+1
            if 0 <= nr < N and 0 <= nc < M:  ## 인덱스 범위를 벗어나지 않고
                if dis[nr][nc] == -1:  ## 아직 최소거리의 값이 없는 곳 == ndis가 최소 거리
                    dis[nr][nc] = nd
                    queue.append((nr, nc, nd))

                    if res < nd:
                        res = nd


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dis = [[-1] * M for _ in range(N)]

sharks = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            sharks.append((i, j, 0))
            dis[i][j] = 0

res = 0
bfs(sharks)

# for i in range(N):
#     print(dis[i])

print(res)




