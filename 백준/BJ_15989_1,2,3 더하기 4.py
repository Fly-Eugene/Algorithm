
import sys
input = sys.stdin.readline

T = int(input())

dp = [[0, 0, 0] ,[1, 0, 0], [1, 1, 0], [1, 1, 1]]
for i in range(4, 10001 + 1):
    tmp_list = []
    tmp_list.append(dp[i - 1][0])
    tmp_list.append(dp[i - 2][0] + dp[i - 2][1])
    tmp_list.append(dp[i - 3][0] + dp[i - 3][1] + dp[i - 3][2])
    dp.append(tmp_list)

for tc in range(T):
    N = int(input())

    print(sum(dp[N]))


