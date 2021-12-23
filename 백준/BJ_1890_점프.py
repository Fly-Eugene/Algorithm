

N = int(input())
arr =[list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for r in range(N):
    for c in range(N):
        if r == N-1 and c == N-1:
            break

        m = arr[r][c]
        if 0 <= r + m < N:
            dp[r + m][c] += dp[r][c]
        if 0 <= c + m < N:
            dp[r][c + m] += dp[r][c]


print(dp[N-1][N-1])




