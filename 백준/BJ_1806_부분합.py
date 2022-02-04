
N, S = map(int, input().split())
arr = list(map(int, input().split()))

right = 0
tmp_sum, tmp_length = 0, 0
res = float('inf')

# print(arr)
for left in range(N):

    while right < N and tmp_sum < S:
        tmp_sum += arr[right]
        tmp_length += 1
        right += 1

    if tmp_sum >= S:
        res = min(tmp_length, res)

    # print('---------------------------------------------')
    # print('left, right', left, right)
    # print('tmp_sum, tmp_length', tmp_sum, tmp_length)

    tmp_sum -= arr[left]
    tmp_length -= 1

if res == float('inf'):
    print(0)
else:
    print(res)

