
n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

arr = [[] for _ in range(k+1)]

for idx in range(k+1):
    new_set = set()

    if idx in coin:
        new_set.add(idx)

    for c in coin:
        n_idx = idx - c
        if 0 <= n_idx:
            for item in arr[n_idx]:
                n_item = []
                if type(item) == int:
                    n_item.append(item)
                else:
                    n_item.extend(list(item))
                n_item.append(c)
                n_item.sort()
                new_set.add(tuple(n_item))

    if new_set == set():
        continue
    arr[idx] = new_set

print(len(arr[k]))
