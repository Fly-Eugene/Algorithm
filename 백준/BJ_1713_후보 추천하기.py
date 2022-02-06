import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
recommends = list(map(int, input().split()))
cnt = [0] * (101)
homepage = [[], []]

for st in recommends:

    cnt[st] += 1
    if cnt[st] == 1:

        if len(homepage[0]) == N:
            min_reco = min(homepage[1])
            idx = homepage[1].index(min_reco)

            del_st = homepage[0].pop(idx)
            homepage[1].pop(idx)

            cnt[del_st] = 0

        homepage[0].append(st)
        homepage[1].append(1)

    else:
        idx = homepage[0].index(st)
        homepage[1][idx] += 1

homepage[0].sort()
print(* homepage[0])
