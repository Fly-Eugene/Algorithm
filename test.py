
dr = [1, 0]
dc = [0, 1]

def dfs(r, c, mamo):

    visited[r][c] = 1

    for i in range(2):
        nr, nc = r + dr[i], c + dc[i]

        if visited[nr][nc] == 0:
            visited[nr][nc] = 1
            n_mamo = mamo + map_arr[nr][nc]
            dfs(nr, nc, n_mamo)


H, W = map(int, input().split())
map_arr = list(map(int, input().split()))
visited = [[0]*W for _ in range(H)]
best_arr = [[0]*W for _ in range(H)]
res = []




