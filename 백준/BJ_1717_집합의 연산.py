import sys
sys.setrecursionlimit(10**6)

def Find_set(x):
    if p[x] == x:
        return x
    else:
        parent = Find_set(p[x])
        p[x] = parent
        return parent

def Union_set(x, y):
    x_parent = Find_set(x)
    y_parent = Find_set(y)

    if x_parent == y_parent:
        return
    elif x_parent < y_parent:
        p[y_parent] = x_parent
    else:
        p[x_parent] = y_parent


N, M = map(int, input().split())
p = [i for i in range(N+1)]
for m in range(M):
    op, a, b = map(int, input().split())
    if op == 0:
        Union_set(a, b)
    else:
        if Find_set(a) == Find_set(b):
            print("YES")
        else:
            print("NO")

