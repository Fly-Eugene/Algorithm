
arr = [[0] * 100 for _ in range(100)]

N = int(input())
for i in range(N):
    r, c = map(int, input().split())
    for nr in range(r, r+10):
        for nc in range(c, c+10):
            if arr[nr][nc] == 0:
                arr[nr][nc] = 1

res = 0
for i in range(100):
    res += sum(arr[i])

print(res)
