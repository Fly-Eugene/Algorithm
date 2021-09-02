from collections import deque

def dfs(start):
    global cnt

    stack = deque()
    stack.append(start)
    visited[start] = 1

    while stack:
        country = stack.popleft()

        for nxt in linked[country]:
            if visited[nxt] == 0:
                cnt += 1
                stack.append(nxt)
                visited[nxt] = 1


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    linked = [[] for _ in range(N+2)]
    visited = [0] * (N+2)
    cnt = 0

    for i in range(M):
        a, b = map(int, input().split())
        linked[a].append(b)
        linked[b].append(a)

    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)

    print(cnt)




