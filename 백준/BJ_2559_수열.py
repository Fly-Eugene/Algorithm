
N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = [0] * (N+1)

for i in range(N):
    arr_sum[i+1] = arr_sum[i] + arr[i]

max_res = -100 * 100000

for right in range(K, N+1):
    res = arr_sum[right] - arr_sum[right-K]

    max_res = max(max_res, res)

print(max_res)

