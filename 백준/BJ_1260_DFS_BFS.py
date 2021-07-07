def dfs(v):
    dfs_visited[v] = 1
    dfs_res.append(v)

    for i in range(N+1):
        if dfs_visited[i] == 0 and arr[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    bfs_visited[v] = 1

    while len(queue) != 0:
        n = queue.pop(0)
        bfs_res.append(n)

        for i in range(N+1):
            if bfs_visited[i] == 0 and arr[n][i] == 1:
                queue.append(i)
                bfs_visited[i] = 1



N, M, V = map(int, input().split())
link_list = [list(map(int, input().split())) for _ in range(M)]
arr = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    r, c = link_list[i]
    arr[r][c] = 1
    arr[c][r] = 1

dfs_visited, dfs_res = [0] * (N+1), []
bfs_visited, bfs_res = [0] * (N+1), []

dfs(V)
bfs(V)


print(*dfs_res)
print(*bfs_res)
