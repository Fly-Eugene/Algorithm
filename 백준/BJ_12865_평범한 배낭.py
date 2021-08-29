
n, k = map(int, input().split())
objects = []

for _ in range(n):
    objects.append(list(map(int, input().split())))

arr = [0] * (k+1)
objects.sort(key = lambda x : x[0], reverse=True)

for ob in objects:
    w, v = ob
    if w < k+1:
        if arr[w] != 0:
            for idx in range(k, w-1, -1):
                if arr[idx] != 0:
                    if idx + w < k+1:
                        arr[idx+w] = max(arr[idx+w], arr[idx] + v)
            arr[w] = max(arr[w], v)
        else:
            arr[w] = v
            for idx in range(k, w, -1):
                if arr[idx] != 0:
                    if idx + w < k+1:
                        arr[idx+w] = max(arr[idx+w], arr[idx] + v)

# print(arr)
print(max(arr))






