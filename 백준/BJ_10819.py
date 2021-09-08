
def calc(sel):
    res = 0
    for i in range(N-1):
        res += abs(sel[i] + sel[i+1])

    return res

def perm(idx):
    global max_sum

    if idx == N:
        res = calc(sel)
        print(res)
        if max_sum < res:
            max_sum = res
        return

    else:
        for i in range(N):
            if chk[i] == 0:
                sel[idx] = nums[i]
                chk[i] = 1
                perm(idx + 1)
                chk[i] = 0


N = int(input())
nums = list(map(int, input().split()))

sel = [0] * N
chk = [0] * N
perm(0)

max_sum = 0







