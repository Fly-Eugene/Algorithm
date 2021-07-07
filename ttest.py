
def cal_weight(left, right, idx):
    print(left, right, idx)

    if idx == N:
        if res.count(abs(sum(left) - sum(right))) == 0:
            res.append(abs(sum(left) - sum(right)))
        return

    else:
        left.append(stones[idx])
        cal_weight(left, right, stones[idx+1])
        left.remove(stones[idx])

        right.append(stones[idx])
        cal_weight(left, right, stones[idx+1])
        right.remove(stones[idx])

        cal_weight(left, right, stones[idx+1])



N = int(input())
stones = list(map(int, input().split()))

left, right = [], []
res = []

cal_weight(left, right, 0)
res.sort()
print(res)


