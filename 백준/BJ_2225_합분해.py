
N, K = map(int, input().split())
arr = [[0] * (N+1) for _ in range(K)]
arr[0] = [1] * (N+1)

for j in range(N+1):
    for i in range(1, K):

        for num in range(j+1):
            cnt = arr[i-1][num]
            arr[i][j] += cnt

print(arr[K-1][N] % 1000000000)

