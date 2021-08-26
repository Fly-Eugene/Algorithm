

N = int(input())
num_list = list(map(int, input().split()))
res_num = num_list.pop()

arr = [[0]*21 for _ in range(N-1)]

for i in range(N-1):
    if i == 0:
        arr[i][num_list[0]] = 1

    else:
        for j in range(21):
            if arr[i-1][j] != 0:
                n_plus = j + num_list[i]
                n_minus = j - num_list[i]
                if 0 <= n_plus <= 20:
                    arr[i][n_plus] += arr[i-1][j]
                if 0 <= n_minus <= 20:
                    arr[i][n_minus] += arr[i-1][j]

print(arr[N-2][res_num])


