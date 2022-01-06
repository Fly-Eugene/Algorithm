
def dijkstra(S, N):
    global INF

    U = [0] * (N+1)
    U[S] = 1

    for v in range(N+1):
        D[v] = adj[S][v]  ## 시작시점에서 시작하는 모든 지점 거리입력

    for _ in range(N):
        # 1. 최소 지점 찾기
        min_w = INF
        next_v = 0

        for i in range(N+1):
            if U[i] == 0 and D[i] < min_w:
                min_w = D[i]
                next_v = i

        U[next_v] = 1
        for i in range(N+1):
            if 0 < adj[next_v][i] < INF:
                D[i] = min(D[i], D[next_v] + adj[next_v][i])

V, E = map(int, input().split())
S = int(input())

INF = 1000001
adj = [[INF]*(V+1) for _ in range(V+1)]
D = [0] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u][v] = w

dijkstra(S, V)

for i in range(1, V+1):
    if i == S:
        print(0)
    elif D[i] == INF:
        print('INF')
    else:
        print(D[i])
