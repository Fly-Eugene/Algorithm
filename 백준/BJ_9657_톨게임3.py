
## 1은 SK, -1는 CY

N = int(input())
arr = [0, 1, -1, 1, 1]

if N <= 4:
    pass
else:
    arr = arr + [0] * (N-4)

    for i in range(5, N+1):
        if -1 in [arr[i-1], arr[i-3], arr[i-4]]:
            arr[i] = 1
        else:
            arr[i] = -1

if arr[N] == 1:
    print('SK')
else:
    print('CY')



