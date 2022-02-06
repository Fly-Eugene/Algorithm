
from collections import defaultdict
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.extend(arr)

sushi_dict = defaultdict(int)
sushi_dict[c] += 1

res = 0

left, right = 0, 0
while right < k:
    sushi_dict[arr[right]] += 1
    right += 1

while right < len(arr):
    res = max(res, len(sushi_dict))

    sushi_dict[arr[left]] -= 1
    sushi_dict[arr[right]] += 1
    if sushi_dict[arr[left]] == 0:
        del sushi_dict[arr[left]]

    left += 1
    right += 1

print(res)
