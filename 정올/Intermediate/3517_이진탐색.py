## 체크할 부분: while low <= high: 이다. 같다가 꼭 들어가야 됨!! 기억할 것

def binary_search(low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        elif arr[mid] == target:
            return mid
        
    return -1


N = int(input())
arr = list(map(int, input().split()))
Q = int(input())
Q_list = list(map(int, input().split()))

res = []
for tr in Q_list:
    res.append(binary_search(0, N-1, tr))

print(*res)


