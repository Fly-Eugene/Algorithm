from math import inf
import heapq

def dijkstra(s, N):

    D[s] = 0
    q = []
    heapq.heappush(q, (0, s))

    while q:
        dis, node = heapq.heappop(q)
        if dis > D[node]:  ## 기록된 길이가 최소길이라면 패스
            continue
        else:
            for adj in adj_list[node]:
                next_node, w = adj[0], adj[1]
                n_w = dis + w
                if n_w < D[next_node]:
                    D[next_node] = n_w
                    heapq.heappush(q, (n_w, next_node))


V, E = map(int, input().split())
s = int(input())
adj_list = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    adj_list[a].append((b, w))

D = [inf] * (V+1)
dijkstra(s, V)

for i in range(1, V+1):
    if D[i] == inf:
        print('INF')
    else:
        print(D[i])