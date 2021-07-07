
N = int(input())
dp = [0] * (N+1)
point_list = [0] * (N+1)

for x in range(1, N+1):
    p = int(input())
    point_list[x] = p
    if x == 1:
        dp[x] = p
    else:
        dp[x] = max(dp[x-2] + p, dp[x-3] + point_list[x-1] + p)

print(dp[N])
# print(dp)



