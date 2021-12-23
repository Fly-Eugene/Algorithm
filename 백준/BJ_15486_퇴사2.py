import sys

N = int(sys.stdin.readline())
times = []
prices = []
dp = [0] * (N+1)

for n in range(N):
    t, p = map(int, sys.stdin.readline().split())
    times.append(t)
    prices.append(p)

for i in range(N):

    t = times[i]

    if i + t <= N:
        # 기존의 값이 클 것인가, 현재의 상담을 통해 더 벌 것인가
        dp[i+t] = max(dp[i+t], dp[i] + prices[i])

    # 다음날에도 최대값을 계속 유지시켜준다.
    dp[i+1] = max(dp[i], dp[i+1])

print(dp[N])