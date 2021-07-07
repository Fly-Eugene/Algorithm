def comb(i, j):
    if i == r:
        print(*sel)
        return

    for k in range(j, N-r+i+1):
        sel[i] = lotto[k]
        comb(i+1, k+1)


lotto = list(map(int, input().split()))
K = lotto.pop(0)
N = len(lotto)
r = 6
sel = [0] * 6

comb(0, 0)




