
N = int(input())
dp = [0] * (N+1)
p = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + p[j])


print(dp[N])