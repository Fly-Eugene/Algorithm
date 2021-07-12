from collections import deque

def dfs(N):
    global INF

    queue = deque()
    queue.append((N, 0))
    time_arr[N] = 0
    cnt_arr[N] = 1


    while queue:
        idx, time = queue.popleft()

        for n_idx in (idx-1, idx+1, idx * 2):
            if 0 <= n_idx < INF:

                if time_arr[n_idx] == -1:
                    time_arr[n_idx] = time + 1
                    cnt_arr[n_idx] = cnt_arr[idx]
                    queue.append((n_idx, time + 1))

                elif time_arr[n_idx] == time_arr[idx] + 1:
                    cnt_arr[n_idx] += cnt_arr[idx]


N, K = map(int, input().split())

INF = 100001
time_arr = [-1 for _ in range(INF)]
cnt_arr = [0 for _ in range(INF)]
dfs(N)

print(time_arr[K])
print(cnt_arr[K])

