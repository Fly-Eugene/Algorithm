import sys


def bin_search(low, high):
    mid, total = 0, 0
    while low < high:
        mid = (low + high) // 2
        total = 0
        cut = trees[mid] # 기준 나무 높이
        for idx in range(mid+1, N):
            total += (trees[idx] - cut)
        if total >= M:
            return mid, total
        else: # 더 베어야 하는 경우
            high = mid
    return mid, total


N, M = map(int, input().split()) # 나무가 N 그루
trees = list(map(int, sys.stdin.readline().split()))
trees.sort()
idx, total = bin_search(0, N-1)
crtr = trees[idx]
# target = N - idx - 1 # 잘리는 나무 갯수

if total == M:
    print(crtr)
elif total > M:
    while total > M:
        crtr += 1
        # total -= target
    if total == M:
        print(crtr)
    elif total < M:
        print(crtr - 1)
else:
    while crtr and total < M:
        crtr -= 1
        total += target
    print(crtr)