
import heapq

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

queue = []
heapq.heappush(queue, (0, 0, 0))
visited[0][0] = 0

while queue:

    cnt, r, c = heapq.heappop(queue)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1:
            if arr[nr][nc] == 0:
                heapq.heappush(queue, (cnt, nr, nc))
                visited[nr][nc] = cnt
            else:
                heapq.heappush(queue, (cnt + 1, nr, nc))
                visited[nr][nc] = cnt + 1

print(visited[N-1][M-1])



