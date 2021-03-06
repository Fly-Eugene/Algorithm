def check(idx):
    who = dp[idx]

    ## 재귀를 벗어나게 해줄 기본 값
    if idx == 1:
        dp[idx] = 'SK'
        return 'CY'     # SK가 첫번째 사람이니까 다음 사람인 CY를 반환해줌

    elif who == 0:
        if 0 < idx-1:
            dp[idx] = check(idx-1)
            if dp[idx] == 'SK':
                return 'CY'
            else:
                return 'SK'
        if 0 < idx-3:
            dp[idx] = check(idx-3)
            if dp[idx] == 'SK':
                return 'CY'
            else:
                return 'SK'

    else:
        if dp[idx] == 'SK':
            return 'CY'
        else:
            return 'SK'

N = int(input())
dp = [0] * (N+1)

check(N)
print(dp[N])

## 0이 SK 1이 CY