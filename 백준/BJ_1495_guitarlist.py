
N, S, M = map(int, input().split())
v_list = list(map(int, input().split()))
dp = [[0] * (M+1) for _ in range(N+1)]

dp[0][S] = 1

for i in range(1, N+1):
    for j in range(M+1):
        if dp[i-1][j] == 0:
            continue
        if 0 <= j - v_list[i-1] <= M:
            dp[i][j-v_list[i-1]] = 1
        if 0 <= j + v_list[i-1] <= M:
            dp[i][j+v_list[i-1]] = 1

ans = -1
for j in range(M, -1, -1):
    if dp[N][j] == 1:
        ans = j
        break

print(ans)





