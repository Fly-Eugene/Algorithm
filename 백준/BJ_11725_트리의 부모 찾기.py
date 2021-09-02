
def dfs():
    stack = [1]

    while stack:
        node = stack.pop(0)
        for nxt in arr[node]:
            if arr[nxt] != 0:
                parent[nxt] = node
                arr[nxt].remove(node)
                stack.append(nxt)

N = int(input())
arr = [[] for _ in range(N+1)]
parent = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs()

for i in range(2, N+1):
    print(parent[i])



