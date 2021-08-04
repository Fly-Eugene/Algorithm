
def factorial(idx):

    if idx == 0:
        dp[idx] = 1
        return 1
    elif dp[idx] == 0:
        dp[idx] = factorial(idx-1) * idx
        return dp[idx]
    else:
        return dp[idx]

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    dp = [0] * (M+1)

    factorial(M)
    res = dp[M] // (dp[N] * dp[M-N])
    print(res)




