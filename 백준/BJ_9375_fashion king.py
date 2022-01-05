
T = int(input())

for tc in range(T):
    N = int(input())
    cloth_dict = {}
    for j in range(N):
        cloth = list(input().split())
        if cloth[1] in cloth_dict:
            cloth_dict[cloth[1]] += 1
        else:
            cloth_dict[cloth[1]] = 1

    res = 1
    for k in cloth_dict:
        res *= (cloth_dict[k] + 1)
    print(res-1)





