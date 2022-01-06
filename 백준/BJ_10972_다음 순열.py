import math


def find_next_perm(order, ans, n):

    if len(ans) == N-1:
        ans.append(num_list_perm[-1])

        return ans
    else:
        termOfNums = math.factorial(n) // n
        idx = math.ceil(order / termOfNums)
        ans.append(num_list_perm.pop(idx))

        return find_next_perm(order-(termOfNums*(idx-1)), ans, n-1)


def find_order(perm, N):
    res = []
    for p in perm:
        termOfNums = math.factorial(N) // N
        idx = num_list.index(p)

        if len(num_list) == 2:
            idx += 1
            res.append(termOfNums*idx)

            return sum(res)
        else:
            num_list.pop(idx)
            res.append(termOfNums*idx)
            N -= 1


N = int(input())
perm = list(map(int, input().split()))
num_list = [i for i in range(1, N+1)]
num_list_perm = [i for i in range(N+1)]

order = find_order(perm, N)

if order == math.factorial(N):
    print(-1)
else:
    ans = find_next_perm(order + 1, [], N)
    print(*ans)
