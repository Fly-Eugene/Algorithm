from collections import deque

def bfs(p, dis, visited):

    queue = deque()
    visited[p] = -1

    for i in range(1, N+1):
        if arr[p][i] == 1:
            queue.append((i, dis + 1))
            visited[i] = dis + 1

    while queue:
        node, d = queue.popleft()

        for i in range(1, N+1):
            if arr[node][i] == 1 and visited[i] == 0:
                queue.append((i, d+1))
                visited[i] = d+1


    return max(visited)


N = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]
friends = [1] * (N+1)
friends[0] = (N+2)

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break

    arr[a][b] = 1
    arr[b][a] = 1


for i in range(1, N+1):
    res = bfs(i, 0, [0] * (N+1))
    friends[i] = res

min_score = min(friends)
print(min_score, friends.count(min_score))
for i in range(1, N+1):
    if friends[i] == min_score:
        print(i, end = ' ')
