
N = int(input())
arr = list(map(int, input().split()))
M = int(input())

arr.sort()

res = 0
left, right = 0, N-1

while left < right:

    tmp_sum = arr[left] + arr[right]

    if tmp_sum == M:
        res += 1
        left += 1
    elif tmp_sum > M:
        right -= 1
    else:
        left += 1

print(res)

