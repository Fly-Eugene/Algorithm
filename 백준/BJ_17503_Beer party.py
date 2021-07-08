
def check(liver):
    res = []
    for beer in beers:
        if beer[1] <= liver:
            res.append(beer[0])

    if len(res) < N:
        return 0

    res.sort()
    return sum(res[-N:])


N, M, K = map(int, input().split())
beers = [tuple(map(int, input().split())) for _ in range(K)]

st_liver = min(i[1] for i in beers)     # 최소 갖춰야 하는 간레벨
en_liver = max(i[1] for i in beers)     # 최대로 설정할 수 있는 간 레벨 => 그 이상을 올릴 필요가 없음

res_liver = 2**31 + 1

while st_liver <= en_liver:
    mid_liver = (st_liver + en_liver) // 2

    if check(mid_liver) >= M:
        en_liver = mid_liver - 1
        res_liver = min(res_liver, mid_liver)

    else:
        st_liver = mid_liver + 1

## 처음 설정한 간 값과 같다는 것은 M 값을 채우는 간 값을 발견하지 못했다는 의미다. 따라서 -1 를 설정함
if res_liver == 2**31 + 1:
    res_liver = -1

print(res_liver)