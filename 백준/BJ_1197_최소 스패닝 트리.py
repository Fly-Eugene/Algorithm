import heapq

def find_set(x):
    if p[x] < 0:
        return x
    else:
        return find_set(p[x])

def union(x, y):
    a = find_set(x)
    b = find_set(y)

    if a == b:
        return

    if p[a] < p[b]:
        p[b] = a
    elif p[b] < p[a]:
        p[a] = b
    else:
        p[a] -= 1
        p[b] = x

def kruskal(graph):
    global mst_cost

    mst = []
    while graph:
        w, a, b = heapq.heappop(graph)
        if find_set(a) != find_set(b):
            union(a, b)
            mst.append((a, b))
            mst_cost += w


V, E = map(int, input().split())
graph = []
for _ in range(E):
    a, b, w = map(int, input().split())
    heapq.heappush(graph, (w, a, b))

p = [-1] * (V+1)  # 상호배타적 집합

mst_cost = 0
kruskal(graph)

print(mst_cost)
