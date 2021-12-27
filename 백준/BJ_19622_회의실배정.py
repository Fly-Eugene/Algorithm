
N = int(input())
arr = [[0] * 4 for _ in range(N)]

for i in range(N):
    s, e, p = map(int, input().split())
    arr[i][0], arr[i][1], arr[i][2] = s, e, p

arr[0][3] = arr[0][2]
res = arr[0][3]

if N >= 2:
    arr[1][3] = arr[1][2]
    res = max(res, arr[1][3])

    if N >= 3:
        arr[2][3] = arr[0][3] + arr[2][2]
        res = max(res, arr[2][3])

        for i in range(3, N):
            arr[i][3] = max(arr[i-2][3], arr[i-3][3]) + arr[i][2]
            res = max(res, arr[i][3])


print(res)


