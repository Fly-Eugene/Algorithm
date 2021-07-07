
def select_sort(num_list):
    idx = 0
    while idx < N-1:
        min_num = 101
        min_idx = 0
        for i in range(idx, N):
            if num_list[i] < min_num:
                min_num = num_list[i]
                min_idx = i

        num_list[idx], num_list[min_idx] = num_list[min_idx], num_list[idx]
        idx += 1
        print(*num_list)


N = int(input())
num_list = list(map(int, input().split()))
select_sort(num_list)

