
def chr_num(num):
    num += 65

    while num < 65 or num > 90:
        if num < 65:
            num += 26
        elif num > 90:
            num -= 26

    return chr(num)


N = int(input())

if 0 < N <= 100 and N % 2:

    arr = [[-1]*N for _ in range(N)]
    num = 0

    for j in range(N//2, -1, -1):
        for i in range(j, N - j):
            arr[i][j] = num
            num += 1

    for i in range(N):
        for j in range(N):
            if arr[i][j] == -1:
                continue
            else:
                print(chr_num(arr[i][j]), end = ' ')
        print()
else:
    print('INPUT ERROR')