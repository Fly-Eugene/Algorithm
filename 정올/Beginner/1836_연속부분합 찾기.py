
N = int(input())
num_list = list(map(int, input().split()))

max_num = -100
for size in range(1, N+1):
    for st in range(N+1-size):
        temp = num_list[st:st+size]

        if max_num < sum(temp):
            max_num = sum(temp)

print(max_num)

