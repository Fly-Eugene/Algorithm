
T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    right, res = 0, 0
    for left in range(N):
        res += right

        while right < M and A[left] > B[right]:
            res += 1
            right += 1

    print(res)



