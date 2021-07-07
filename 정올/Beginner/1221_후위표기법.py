
N = int(input())
mix_list = list(input().split())
num_list = []

for i in range(N):
    if mix_list[i] in ('+', '-', '/', '*'):
        n2 = num_list.pop()
        n1 = num_list.pop()

        if mix_list[i] == '+':
            res = n1 + n2
            num_list.append(res)
        elif mix_list[i] == '-':
            res = n1 - n2
            num_list.append(res)
        elif mix_list[i] == '/':
            res = n1 // n2
            num_list.append(res)
        else:
            res = n1 * n2
            num_list.append(res)
    else:
        num_list.append(int(mix_list[i]))

print(*num_list)

