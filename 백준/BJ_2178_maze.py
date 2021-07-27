dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, dis):
    queue = [(r, c, dis)]

    while len(queue) != 0:
        r, c, dis = queue.pop(0)
        if dis == 1:
            arr[r][c] = -1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1:
                    arr[nr][nc] = dis + 1
                    queue.append((nr, nc, dis + 1))

                # elif arr[nr][nc] != 0 and arr[nr][nc] > dis:
                #     arr[nr][nc] = dis
                #     queue.append((nr, nc, dis + 1))




N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
arr[0][0] = 0

bfs(0, 0, 1)
print(arr[N-1][M-1])



