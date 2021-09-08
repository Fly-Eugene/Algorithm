
def perm(idx):
    if idx == N:
        print(*sel)
        return

    for i in range(N):
        if chk[i] == 0:
            sel[idx] = i + 1
            chk[i] = 1
            perm(idx + 1)

            chk[i] = 0


N = int(input())
sel = [0] * N
chk = [0] * N

perm(0)



