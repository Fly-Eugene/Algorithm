
print(chr(65))

name_list = ["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"]
N = len(name_list)
dup_list = [['']*N, [0]*N]
res = [''] * N

dup_idx = 0

for idx in range(N):
    find_dup = False

    for i in range(N):
        if dup_list[0][i] == name_list[idx]:
            res[idx] = name_list[idx] + chr(65 + dup_list[1][i])
            dup_list[1][i] += 1
            find_dup = True
            break

    if find_dup == False:
        res[idx] = name_list[idx] + chr(65)
        dup_list[0][dup_idx] = name_list[idx]
        dup_list[1][dup_idx] = 1
        dup_idx += 1

print(res)



