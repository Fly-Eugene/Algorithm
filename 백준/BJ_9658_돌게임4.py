
N = int(input())
dp = [0, 1, -1, 1, -1]

if N <= 4:
    pass
else:
    dp += [0] * (N-4)
    for i in range(5, N+1):
        if 1 in [dp[i-1], dp[i-3], dp[i-4]]:
            dp[i] = -1
        else:
            dp[i] = 1

# print(dp)
# print(dp[N])
if dp[N] == -1:
    print('SK')
else:
    print('CY')

