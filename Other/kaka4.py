def f(i):  # i c[i], j= 선택 구간의 시작
    if i == M:
        print(c)
    else:
        for k in range(N):
            c[A[k]] += 1
            f(i + 1)
            c[A[k]] -= 1


N, M = 10, 10
A = [i for i in range(N)]
c = [0] * N



