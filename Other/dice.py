
def type1(idx):
    if idx == cnt:
        print(*sel)
        return

    else:
        for i in range(1, 7):
            sel[idx] = i
            type1(idx + 1)

def type2(idx):
    if idx == cnt:
        if tuple(sorted(sel)) in type_set:
            return
        else:
            print(*sel)
            type_set.add(tuple(sorted(sel)))
            return
    else:
        for i in range(1, 7):
            sel[idx] = i
            type2(idx + 1)


## 조합
def type3(idx, j):
    if idx == cnt:
        print(*sel)
        return

    else:
        for k in range(idx, 6-cnt+idx+1):
            sel[idx] = arr[k]
            type3(idx+1, j+1)


cnt, type = map(int, input().split())
sel = [0] * cnt
arr = [i for i in range(1, 7)]
type_set = set()

if type == 1:
    type1(0)
elif type == 2:
    type2(0)
else:
    type3(0, 0)

