
N = int(input())
jump = list(map(int, input().split()))
dp = [-1] * N
dp[0] = 0

for i in range(N):
    if dp[i] == -1:
        continue

    a = jump[i]
    next = i+a+1
    if next > N:
        next = N
    for j in range(i+1, next):
        if dp[j] == -1:
            dp[j] = dp[i] + 1

print(dp[N-1])



