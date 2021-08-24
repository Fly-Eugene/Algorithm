
N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(input()))

dp = [0]*N
dp[0] = num_list[0]

if N > 1:
    dp[1] = num_list[0] + num_list[1]

    if N > 2:
        dp[2] = max(num_list[0] + num_list[2], num_list[0]+num_list[1], num_list[1]+num_list[2])
        for i in range(3, N):
            dp[i] = max(dp[i-1], dp[i-3]+num_list[i-1]+num_list[i], dp[i-2]+num_list[i])

print(max(dp))
