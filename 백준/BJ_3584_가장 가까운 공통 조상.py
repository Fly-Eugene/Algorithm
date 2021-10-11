import sys
sys.setrecursionlimit(100000)

def Find_set(x, arr):
    if p[x] == x:
        return arr
    else:
        arr.append(p[x])
        return Find_set(p[x], arr)


T = int(input())
for tc in range(T):
    N = int(input())
    p = [i for i in range(N+1)]
    for i in range(N-1):
        parent, child = map(int, input().split())
        p[child] = parent

    a_node, b_node = map(int, input().split())
    a_parents = Find_set(a_node, [a_node])
    b_parents = Find_set(b_node, [b_node])
    res = 0
    for a in a_parents:
        if a in b_parents:
            res = a
            break

    print(res)


