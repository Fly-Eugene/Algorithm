
def cut(r, c, n):
    global blue_cnt, white_cnt

    color = arr[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if color != arr[i][j]:
                cut(r, c, n//2)
                cut(r, c + n//2, n//2)
                cut(r + n//2, c, n//2)
                cut(r + n//2, c + n//2, n//2)
                return

    if color == 0:
        white_cnt += 1
        return

    else:
        blue_cnt += 1
        return



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

blue_cnt = 0
white_cnt = 0

cut(0, 0, N)
print(white_cnt)
print(blue_cnt)