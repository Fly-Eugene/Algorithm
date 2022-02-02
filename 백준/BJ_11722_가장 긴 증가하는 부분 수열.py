
N = int(input())
arr = list(map(int, input().split()))
dp = [1] * (N)

for i in range(N):
    num = arr[i]
    for j in range(i, -1, -1):
        if num < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))



