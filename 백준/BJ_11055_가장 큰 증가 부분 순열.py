
N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
dp[0] = 1

for i in range(N):
    num = arr[i]
    max_sum = 0

    for j in range(i-1, -1, -1):
        if arr[j] < num and max_sum < dp[j]:
            max_sum = dp[j]

    dp[i] = arr[i] + max_sum

print(max(dp))




