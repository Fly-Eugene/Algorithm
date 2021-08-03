
N = int(input())
arr = list(input())
cnt = 0

for i in range(0, N-3):
    if arr[i] == 'p':
        if arr[i+1] == 'P' and arr[i+2] == 'A' and arr[i+3] == 'p':
            arr[i], arr[i+1], arr[i+2], arr[i+3] = 0, 0, 0, 0
            cnt += 1

    else:
        continue

print(cnt)
