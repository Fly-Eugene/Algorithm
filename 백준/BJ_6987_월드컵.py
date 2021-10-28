
def comb(i, j):
    if i == 2:
        comb_list.append(comb_res)
        return

    else:
        for k in range(j, 6-2+i+1): ## range(j, n-r+i+1)
            comb_res[i] = team[k]
            comb(i+1, j+1)


results = [[0, 0, 0] * 6 for _ in range(3)]

team = [i for i in range(6)]
comb_res = [0, 0]
comb_list = []
comb(0, 0)

for comb_item in comb_list:
    a, b = comb_item

    # 무승부 일때
    for i in range(3):
        results[i][a * 3 + 1] += 1
        results[i][b * 3 + 1] += 1

    # a 승, b 패
    for i in range(3):
        results[i][a * 3] += 1
        results[i][b * 3 + 2] += 1

    # a 패, b 승
    for i in range(3):
        results[i][a * 3 + 2] += 1
        results[i][b * 3] += 1





