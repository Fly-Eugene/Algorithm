import heapq
from math import inf

def dijkstra(S, N):

    D[S] = 0
    q = []
    heapq.heappush(q, (0, S))

    while q:
        dist, node = heapq.heappop(q)
        if dist > D[node]:
            continue
        for adj in adj_list[node]:
            next_node, w = adj[0], adj[1]
            n_w = dist + w
            if D[next_node] > n_w:
                D[next_node] = n_w
                heapq.heappush(q, (n_w, next_node))



N = int(input())
M = int(input())

adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    adj_list[a].append((b, w))

S, E = map(int, input().split())
D = [inf] * (N+1)

dijkstra(S, N)
print(D[E])

