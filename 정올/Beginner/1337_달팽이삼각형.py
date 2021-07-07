
N = int(input())
snail = [[-1]*(N) for _ in range(N)]
snail[0][0] = 0

num = 1
r, c = 0, 0
for i in range(N):

    if i % 3 == 0:
        if i == 0:
            for j in range(N - i - 1):
                r, c = r+1, c+1
                snail[r][c] = str(num)[-1]
                num += 1
        else:
            for j in range(N - i):
                r, c = r+1, c+1
                snail[r][c] = str(num)[-1]
                num += 1

    elif i % 3 == 1:
        for j in range(N - i):
            c -= 1
            snail[r][c] = str(num)[-1]
            num += 1

    elif i % 3 == 2:
        for j in range(N - i):
            r -= 1
            snail[r][c] = str(num)[-1]
            num += 1


for i in range(N):
    res = snail[i][:i+1]
    print(*res)
