
N = int(input())
arr = [1 for _ in range(10)]

for i in range(N-1):
    for j in range(1, 10):
        arr[j] += arr[j-1]

print(sum(arr) % 10007)
