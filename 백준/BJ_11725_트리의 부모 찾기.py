def bfs():
    queue = []
    for i in range(1, N+1):
        if arr[1][i] == 1:
            queue.append((1, i))
            parent[i] = 1
            arr[i][1], arr[1][i] = 0, 0

    while queue:
        r, c = queue.pop(0)
        for i in range(1, N+1):
            if arr[c][i] == 1:
                queue.append((1, i))
                parent[i] = c
                arr[c][i], arr[i][c] = 0, 0



N = int(input())
nodes = [list(map(int, input().split())) for _ in range(N-1)]
arr = [[0]*(N+1) for _ in range(N+1)]
parent = [0] * (N+1)

for node in nodes:
    r, c = node
    arr[r][c] = 1
    arr[c][r] = 1

bfs()

for idx in range(2, N+1):
    print(parent[idx])
