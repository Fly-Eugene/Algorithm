
max_N = 101
pado = [0] * max_N
pado[0], pado[1], pado[2] = 1, 1, 1

for i in range(3, max_N):
    if i % 3 == 2:
        pado[i] = pado[i-3] + pado[i-4] + pado[i-5]
    else:
        pado[i] = pado[i-2] + pado[i-3]


T = int(input())
for tc in range(T):
    N = int(input())
    print(pado[N-1])

