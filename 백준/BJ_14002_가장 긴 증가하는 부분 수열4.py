
N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1


max_cnt, find_cnt = max(dp), max(dp)
res = []

for back_idx in range(N-1, -1, -1):
    if dp[back_idx] == find_cnt:
        res.append(arr[back_idx])
        find_cnt -= 1

res.sort()
print(max_cnt)
print(*res)




