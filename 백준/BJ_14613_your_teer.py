
w, l, d = map(float, input().split())

dp = [[0] * (3501) for _ in range(20)]
dp[0][2000] = 1

for i in range(19):
    for j in range(len(dp[i])):
        if dp[i][j] != 0:
            if j + 50 < len(dp[i]):
                dp[i+1][j+50] += dp[i][j] * w
            if 0 <= j - 50:
                dp[i+1][j-50] += dp[i][j] * l
            dp[i+1][j] += dp[i][j] * d

bronze = sum(dp[19][1000:1499])
silver = sum(dp[19][1500:2000])
gold = sum(dp[19][2000:2500])
platinum = sum(dp[19][2500:3000])
dia = sum(dp[19][3000:3500])

print(round(bronze, 8))
print(round(silver, 8))
print(round(gold, 8))
print(round(platinum, 8))
print(round(dia, 8))
