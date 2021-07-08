def cal(h):
    tree_length = 0
    for tree in trees:
        if tree <= h:
            continue
        else:
            tree_length += (tree - h)

    return tree_length

def cutting(st, en):
    global res

    while st <= en:
        mid = (st + en) // 2
        if cal(mid) < M:
            en = mid - 1

        elif cal(mid) > M:
            st = mid + 1
            res = max(mid, res)

        elif cal(mid) == M:
            res = mid
            return



N, M = map(int, input().split())
trees = list(map(int, input().split()))
res = 0

cutting(0, max(trees))
print(res)

