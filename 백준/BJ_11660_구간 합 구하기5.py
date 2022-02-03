
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for i in range(N+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] - dp[i][j]) + box[i][j]

# for i in range(N+1):
#     print(dp[i])

for m in range(M):
    r1, c1, r2, c2 = map(int, input().split())
    print(dp[r2][c2] - (dp[r1-1][c2] + dp[r2][c1-1] - dp[r1-1][c1-1]))



