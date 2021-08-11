
N, M = map(int, input().split())
places = [list(map(int, input().split())) for _ in range(N)]
places.append([0,0])
places.sort(key=lambda x: (x[0], x[1]))

dp = [[0,0,0] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(i):
        # print('=====================================')
        # print('현재 i, j는', i, j)
        diff_r = places[i][0] - places[j][0]
        diff_c = places[i][1] - places[j][1]
        # print('둘의 차이는', diff_r, diff_c)

        if diff_r >= 0 and diff_c >= 0:

            if dp[i][2] < M * (dp[j][0] + 1) - (diff_r + diff_c + (dp[j][1] * 2)):
                # print('i의 cnt 개수가 더 작다')
                # print('새로운 거리는', diff_r+diff_c+dp[j][1])
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = diff_r + diff_c + (dp[j][1] * 2)
                dp[i][2] = M * (dp[j][0] + 1) - (diff_r + diff_c + (dp[j][1] * 2))


res = 0
for i in range(N+1):
    if res < dp[i][2]:
        res = dp[i][2]


print(dp)
print(res)
