
n = int(input())

snail = [[0]*n for _ in range(n)]
snail[0][0] = 1

r, c = 0, 0
cnt = n
num = 2

for i in range(n * 2 - 1):
    if i % 4 == 0:
        if i == 0:
            for i in range(n-1):
                c += 1
                snail[r][c] = num
                num += 1
        else:
            for i in range(cnt):
                c += 1
                snail[r][c] = num
                num += 1

    elif i % 4 == 1:
        cnt -= 1
        for i in range(cnt):
            r += 1
            snail[r][c] = num
            num += 1

    elif i % 4 == 2:
        for i in range(cnt):
            c -= 1
            snail[r][c] = num
            num += 1

    elif i % 4 == 3:
        cnt -= 1
        for i in range(cnt):
            r -= 1
            snail[r][c] = num
            num += 1


for i in range(n):
    print(*snail[i])
