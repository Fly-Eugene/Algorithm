
def bfs():
    global cnt

    queue = [1]
    visited[1] = 1

    while queue:
        p = queue.pop(0)
        for i in range(N+1):
            if arr[p][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                cnt += 1



N = int(input())
M = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1



cnt = 0
bfs()
print(cnt)
