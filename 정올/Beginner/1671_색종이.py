
arr = [[0] * 101 for _ in range(101)]

N = int(input())

for _ in range(N):
    c, r = map(int, input().split())

    for nr in range(r, r+10):
        if nr == r or nr == r + 9:
            for nc in range(c, c+10):
                if arr[nr][nc] == 0:
                    arr[nr][nc] = 2
        else:
            if arr[nr][c] == 0:
                arr[nr][c] = 2
            if arr[nr][c+9] == 0:
                arr[nr][c+9] = 2
            for nc in range(c+1, c+9):
                arr[nr][nc] = 1


res = 0
for i in range(100):
    print(arr[i])
    res += arr[i].count(-1)

print(res)

