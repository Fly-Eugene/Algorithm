
def in_order(st, end, depth):
    global res

    if st > end:
        return

    else:
        mid = (st + end) // 2
        res[depth].append(visit[mid])
        in_order(st, mid-1, depth+1)
        in_order(mid+1, end, depth+1)



k = int(input())
visit = list(map(int, input().split()))
res = [[] for _ in range(k)]

in_order(0, 2 ** k - 2, 0)

for i in range(k):
    print(*res[i])