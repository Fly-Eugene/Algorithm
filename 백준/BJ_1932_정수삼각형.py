
N = int(input())
tri = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = tri[0][0]   # 맨꼭대기 값 넣어주기

for i in range(N-1):
    for j in range(i+1):
        r = i+1
        c1, c2 = j, j+1      # 현재 위치에서 새롭게 갈 수 있는 위치 (i+1, j) (i+1, j+1)

        if dp[r][c1] < tri[r][c1] + dp[i][j]:
            dp[r][c1] = tri[r][c1] + dp[i][j]

        if dp[r][c2] < tri[r][c2] + dp[i][j]:
            dp[r][c2] = tri[r][c2] + dp[i][j]

print(max(dp[N-1]))