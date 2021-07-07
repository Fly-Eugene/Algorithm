
n = int(input())
zz = [[0]*n for _ in range(n)]
zz[0][0] = 1

r, c = 0, 0
cnt = 0
num = 2
stop = 0

while cnt < n//2 + 1:

    # 한 칸 내린다
    r += 1
    zz[r][c] = num
    num += 1

    # 위쪽 대각선으로 움직인다.
    cnt += 1
    for i in range(cnt):
        r, c = r-1, c+1

        zz[r][c] = num
        num += 1

    if n % 2 == 0 and cnt == n//2 + 1:
        break

    # 오른쪽으로 한칸 움직인다.
    c += 1
    zz[r][c] = num
    num += 1

    # 아래 대각선으로 움직인다.
    cnt += 1
    for i in range(cnt):
        r, c = r+1, c-1
        zz[r][c] = num
        num += 1

while cnt > 0:

    # 오른쪽으로 한 칸 움직인다.
    if n % 2:
        c += 1
        zz[r][c] = num
        num += 1
    else:
        r += 1
        zz[r][c] = num
        num += 1

    if n % 2 == 0 and r == n-1 and c == n-1:
        break

    # 위쪽 대각선으로 움직인다.
    cnt -= 1
    for i in range(cnt):
        r, c = r-1, c+1
        zz[r][c] = num
        num += 1

    # 아래로 한 칸 움직인다.
    if n % 2:
        r += 1
        zz[r][c] = num
        num += 1
    else:
        c += 1
        zz[r][c] = num
        num += 1

    # 아래 대각선으로 움직인다.
    cnt -= 1
    for i in range(cnt):
        r, c = r+1, c-1
        zz[r][c] = num
        num += 1


for i in range(n):
    print(*zz[i])


