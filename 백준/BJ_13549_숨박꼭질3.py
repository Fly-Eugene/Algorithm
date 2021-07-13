from collections import deque

def bfs(N):
    queue = deque()
    queue.append((N, 0))
    time_arr[N] = 0

    while queue:
        now, time = queue.popleft()

        for new in (now-1, now+1, now*2):
            if 0 <= new < INF and time_arr[new] == -1:
                if new == now*2:
                    time_arr[new] = time
                    queue.appendleft((new, time))
                else:
                    time_arr[new] = time + 1
                    queue.append((new, time + 1))


N, K = map(int, input().split())
INF = 100001
time_arr = [-1] * INF

bfs(N)

print(time_arr[K])
