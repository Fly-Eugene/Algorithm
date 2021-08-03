def check(idx):
    who = dp[idx]

    if idx == 1:
        dp[idx] = 'SK'
        return

    elif who == 0:
        if 0 < idx-1:
            dp[idx] = check(idx-1)
            return dp[idx]
        elif 0 < idx-3:
            dp[idx] = check(idx-3)
            return dp[idx]
        else:
            return

    else:
        if dp[idx] == 'SK':
            return 'CY'
        else:
            return 'SK'

N = int(input())
dp = [0] * (N+1)

check(N)
print(dp)
print(dp[N])

## 0이 SK 1이 CY