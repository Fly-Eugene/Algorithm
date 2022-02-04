
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

right = 1
res = float('inf')

for left in range(N):

    while right < N:
        diff = arr[right] - arr[left]
        if diff >= M:
            res = min(res, diff)
            break

        right += 1


print(res)