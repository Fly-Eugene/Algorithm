
T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    res = M
    rel = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        for node in rel[b]:
            if a in rel[node]:
                res -= 1

        else:
            rel[a].append(b)
            rel[b].append(a)

    print(res)
