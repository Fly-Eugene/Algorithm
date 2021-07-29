
def comb(idx, j):
    if idx == r:
        sel.sort()
        print(*sel)
        return

    for k in range(j, N-r+idx+1):
        sel[idx] = num_list[k]
        comb(idx+1, k+1)


while True:
    num_list = list(map(int, input().split()))
    k = num_list.pop(0)

    if k == 0:
        break

    N = len(num_list)
    r = 6
    sel = [0] * r
    # 함수 실행
    comb(0, 0)
    print()

