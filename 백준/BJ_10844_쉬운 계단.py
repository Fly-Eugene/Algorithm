
N = int(input())
arr = [[0]*10 for _ in range(N)]

for i in range(N):
    for j in range(10):
        if i == 0:
            ## 처음 시작이 0일수는 없으니 continue
            if j == 0: continue
            ## 그 외에는 모두 1로 초기화
            arr[i][j] = 1
        else:
            if j == 0:
                arr[i][j] = arr[i-1][j+1]
            elif j == 9:
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]

print(sum(arr[N-1]) % 1000000000)


