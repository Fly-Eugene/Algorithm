
def num_to_chr(num):
    num += 65

    while num < 65 or num > 90:
        if num < 65:
            num += 26
        elif num > 90:
            num -= 26

    return chr(num)


N = int(input())

diamond = [[-1]*(N*2-1) for _ in range(N*2-1)]
diamond[0][N-1] = 0

num = 1
cnt = N-1
r, c = 0, N-1

while cnt > 0:

    for i in range(cnt):
        r, c = r+1, c-1
        diamond[r][c] = num
        num += 1

    for i in range(cnt):
        r, c = r+1, c+1
        diamond[r][c] = num
        num += 1

    for i in range(cnt):
        r, c = r-1, c+1
        diamond[r][c] = num
        num += 1

    cnt -= 1
    for i in range(cnt):
        r, c = r-1, c-1
        diamond[r][c] = num
        num += 1

    c -= 1
    diamond[r][c] = num
    num += 1

diamond[N-1][N-1] = num - 1


for i in range(len(diamond)):
    ## 공백 만드는 과정
    if i <= len(diamond) // 2:
        print(' ' * ((N-i-1) * 2), end = '')
    else:
        print(' ' * ((i - (N-1)) * 2), end = '')

    # 뒤에 알파벳 뽑는 과정
    for j in range(len(diamond[i])):
        if diamond[i][j] == -1:
            continue
        print(num_to_chr(diamond[i][j]), end = ' ')

    print()


