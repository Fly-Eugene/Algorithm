from itertools import permutations

def perm(idx):
    global N

    if idx == N-1:
        calc(sel)
        return

    else:
        for i in range(N-1):
            if visited[i] == 0 and (i == 0 or operator[i] != operator[i-1] or visited[i-1]):
                sel[idx] = operator[i]
                visited[i] = 1
                perm(idx+1)
                visited[i] = 0

def calc(sel):
    global nums, max_num, min_num

    res = nums[0]
    for i in range(1, N):
        if sel[i-1] == 0:  # 덧셈
            res += nums[i]
        elif sel[i-1] == 1:
            res -= nums[i]
        elif sel[i-1] == 2: # 곱셈
            res *= nums[i]
        else:
            if res < 0:
                res = - (abs(res) // nums[i])
            else:
                res //= nums[i]

    if res < min_num:
        min_num = res
    if res > max_num:
        max_num = res

    return


N = int(input())
nums = list(map(int, input().split()))
temp = list(map(int, input().split()))
operator = []

for i in range(4):
    operator.extend([i] * temp[i])

sel = [0] * (N-1)
visited = [0] * (N-1)
min_num = 1000000000000000
max_num = -1000000000000000


perm(0)
print(max_num)
print(min_num)







