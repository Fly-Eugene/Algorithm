
def cnt_insert():
    cnt = 0
    for end in range(1, N):
        for i in range(end-1, -1, -1):
            if num_list[i] > num_list[i+1]:
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
                cnt += 1
            else:
                break
    return cnt

N = int(input())
num_list = list(map(int, input().split()))
res = cnt_insert()
print(res)