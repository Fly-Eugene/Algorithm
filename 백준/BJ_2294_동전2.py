
N, K = map(int, input().split())
dp = [-1] * (K+1)
coin = []

for i in range(N):
    v = int(input())
    coin.append(v)
    if v < K+1:
        dp[v] = 1

for i in range(1, K+1):
    for j in coin:
        if i-j > 0 and dp[i-j] != -1:
            if dp[i] == -1:
                dp[i] = dp[i-j] + 1
            else:
                dp[i] = min(dp[i], dp[i-j] + 1)

print(dp[K])
