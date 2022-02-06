import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
cnt = 0

for i in range(N):
    tmp_list = arr[:i] + arr[i+1:]
    left, right = 0, len(tmp_list) - 1

    while left < right:
        tmp_sum = tmp_list[left] + tmp_list[right]
        if tmp_sum == arr[i]:
            cnt += 1
            break

        if tmp_sum < arr[i]:
            left += 1
        else:
            right -= 1

print(cnt)