
## 1은 SK, -1는 CY

N = int(input())
arr = [0] * (N+1)
arr[1], arr[3], arr[4] = 1, 1, 1
arr[2] = -1


if N <= 4:
    pass
else:
    for i in range(5, N+1):
        if -1 in [arr[i-1], arr[i-3], arr[i-4]]:
            arr[i] = 1
        else:
            arr[i] = -1

if arr[N] == 1:
    print('SK')
else:
    print('CY')



