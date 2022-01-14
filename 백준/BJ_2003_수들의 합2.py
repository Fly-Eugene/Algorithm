
N, M = map(int, input().split())
arr = list(map(int, input().split()))

end = 0
tmp_sum = 0
cnt = 0

for st in range(N):

    while end < N and tmp_sum < M:  ## end의 인덱스 초과가 나지 않고, tmp_sum 이 M보다 작은 경우 계속 오른쪽으로 이동
        tmp_sum += arr[end]
        end += 1

    if tmp_sum == M:
        cnt += 1
        # print("발견함", st, end)

    tmp_sum -= arr[st]

print(cnt)


