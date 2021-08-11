
dr = [-1, -2, 1, 2, -2, -1, 2, 1]
dc = [-2, -1, -2, -1, 1, 2, 1, 2]

def bfs(r, c, cnt):
    queue = [(r, c, cnt)]
    arr[r][c] = cnt

    while queue:
        r, c, cnt = queue.pop(0)
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == -1:
                    arr[nr][nc] = cnt + 1
                    queue.append((nr, nc, cnt + 1))

                if nr == goal_r and nc == goal_c:
                    return


T = int(input())

for tc in range(T):
    N = int(input())
    r, c = map(int, input().split())
    goal_r, goal_c = map(int, input().split())
    arr = [[-1] * (N+1) for _ in range(N+1)]
    bfs(r, c, 0)

    # for i in range(N+1):
    #     print(arr [i])
    print(arr[goal_r][goal_c])


