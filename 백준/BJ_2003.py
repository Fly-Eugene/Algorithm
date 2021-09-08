
n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

for i in range(n):
    for j in range(i, n):
        res = sum(nums[i:j+1])
        if res == s:
            cnt += 1

print(cnt)
