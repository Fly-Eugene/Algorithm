
N = int(input())
power = list(map(int, input().split()))
dp = [1] * N
sel = [0] * (N+1)
sel[1] = 1
res = 0

for i in range(1, N):
    p = power[i]
    max_cnt = 0


    for j in range(i, -1, -1):
        if p < power[j] and max_cnt < dp[j]:
            max_cnt = dp[j]

    dp[i] = max_cnt + 1
    if sel[dp[i]] == 0:
        sel[dp[i]] = 1
    else:
        res += 1


# print(dp)
print(res)


