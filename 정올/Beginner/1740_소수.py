
import math

m = int(input())
n = int(input())

arr = [-1, -1] + [0] * (n-1)

# 소수여부 판별하기, 에라토스테네스의 체
for i in range(int(math.sqrt(n)) + 1):
    if arr[i] == 0:
        check = i*2

        while check <= n:
            arr[check] = 1
            check += i

    else:
        continue

# print(arr)

res = 0
res_first = 0
first = True

for idx in range(m, n+1):

    if arr[idx] == 0 and first:
        res += idx
        res_first = idx
        first = False

    elif arr[idx] == 0:
        res += idx

if res == 0:
    print(-1)
else:
    print(res)
    print(res_first)


