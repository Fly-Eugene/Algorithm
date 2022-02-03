
N = int(input())

tri_one = [0, 1]
tri_two = [0, 1]

idx = 2
while N >= tri_two[-1]:
    tri_one.append(tri_one[idx-1] + idx)
    tri_two.append(tri_two[idx-1] + tri_one[idx])
    idx += 1

dp = [float('inf')] * (N+1)

for st_num in tri_two:
    if st_num <= N:
        dp[st_num] = 1

for i in range(1, N+1):
    for j in range(len(tri_two)-1, 0, -1):
        tri_num = tri_two[j]
        if tri_num <= N:
            dp[i] = min(dp[i], dp[i-tri_num] + 1)

print(dp)
print(dp[N])



