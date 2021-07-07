
N = int(input())

dir_length = [[] for _ in range(4)]
minus_area  = 1

for _ in range(6):
    dir, length = map(int, input().split())
    dir_length[dir-1].append(length)

if len(dir_length[0]) == len(dir_length[2]) == 2:
    minus_area = dir_length[0][0] * dir_length[2][1]
elif len(dir_length[1]) == len(dir_length[2]) == 2:
    minus_area = dir_length[1][0] * dir_length[2][1]
elif len(dir_length[1]) == len(dir_length[3]) == 2:
    minus_area = dir_length[1][1] * dir_length[3][1]
elif len(dir_length[0]) == len(dir_length[3]) == 2:
    minus_area = dir_length[0][1] * dir_length[3][0]


print(dir_length)
print(minus_area)
all_area = sum(dir_length[0]) * sum(dir_length[2])
res = (all_area - minus_area) * N
print(res)

