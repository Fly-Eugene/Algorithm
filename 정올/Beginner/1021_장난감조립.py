

def make_toy(n, k):

    for mini_idx in range(len(toy_list[n])):
        if toy_list[toy_list[n][mini_idx]] == []:
            basic_toy[toy_list[n][mini_idx]] += toy_cnt[n][mini_idx] * k

        else:
            make_toy(toy_list[n][mini_idx], k * toy_cnt[n][mini_idx])


N = int(input())
M = int(input())

toy_list = [[] for _ in range(N+1)]
toy_cnt = [[] for _ in range(N+1)]

basic_toy = [0] * (N+1)

for i in range(M):
    x, y, k = map(int, input().split())
    toy_list[x].append(y)
    toy_cnt[x].append(k)

# print(toy_list)
# print(toy_cnt)


make_toy(N, 1)
for i in range(1, N+1):
    if basic_toy[i] != 0:
        print(i, basic_toy[i])
    else:
        continue


