from collections import deque

def bfs(N, K):

    queue = deque()
    queue.append((N, 0))
    time_history[N][0] = 0

    while queue:
        now, time = queue.popleft()
        if now == K:
            return

        for new in (now-1, now+1, now*2):
            if 0 <= new < INF and time_history[new][0] == -1:
                time_history[new][0] = time + 1
                time_history[new][1] = str(now)
                queue.append((new, time + 1))

N, K = map(int, input().split())
INF = 100001
time_history = [[-1, '_'] for _ in range(INF)]

bfs(N, K)
print(time_history[K][0])
res = []

idx = K
while True:
    if idx == N:
        break
    elif time_history[K][1]:
        res.append(time_history[idx][1])
        idx = int(time_history[idx][1])

res.reverse()
res.append(K)
print(*res)

