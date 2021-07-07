

for tc in range(int(input())):

    N = int(input())
    wear = {}

    for i in range(N):
        item, type = map(str, input().split())
        if type in wear:
            wear[type].append(item)
        else:
            wear[type] = [item]

    wear_values = list(wear.values())
    res = 1

    if len(wear_values) == 1:
        res = len(wear_values[0])
    else:
        for i in range(len(wear_values)):
            res *= (len(wear_values[i])+1)

        res -= 1
    print(res)
