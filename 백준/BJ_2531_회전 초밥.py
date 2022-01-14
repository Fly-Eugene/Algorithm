
from collections import defaultdict

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.extend(arr)

left, right = 0, 0
sushi_dict = defaultdict(int)
result = 0

sushi_dict[c] += 1

while right < k:
    sushi_dict[arr[right]] += 1
    right += 1

while right < len(arr):
    result = max(result, len(sushi_dict))

    sushi_dict[arr[left]] -= 1
    if sushi_dict[arr[left]] == 0:
        del sushi_dict[arr[left]]

    sushi_dict[arr[right]] += 1
    left += 1
    right += 1

print(result)


