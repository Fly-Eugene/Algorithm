def comb(i, j):
    if i == r:
        if tuple(sorted(sel)) not in duple_set:
            duple_set.add(tuple(sorted(sel)))
        return

    for k in range(j, N-r+i+1):
        sel[i] = num_list[k]
        comb(i+1, k+1)


N, r = map(int, input().split())
comb_ex = tuple(map(int, input().split()))

num_list = [i for i in range(1, N+1)]
duple_set = set()
sel = [0] * r

comb(0, 0)

duple_list = sorted(list(duple_set))

if duple_list.index(comb_ex) == len(duple_list) - 1:
    print("NONE")
else:
    print(*duple_list[duple_list.index(comb_ex) + 1])



