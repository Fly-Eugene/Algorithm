import heapq

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    a, b = find_set(x), find_set(y)

    if a < b:
        p[b] = a
    else:
        p[a] = b

def kruskal():
    global res, cnt

    while True:
        if cnt == N-1:
            return
        else:
            c, a, b = heapq.heappop(graph)
            if find_set(a) != find_set(b):
                union(a, b)
                res += c
                cnt += 1


N = int(input())
M = int(input())

graph = []
for i in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(graph, (c, a, b))

cnt, res = 0, 0
p = [i for i in range(N+1)]

kruskal()
print(res)
