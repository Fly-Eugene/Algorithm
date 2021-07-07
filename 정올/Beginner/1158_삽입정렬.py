
def insert_sort(num_list):
    for e in range(1, len(num_list)):
        for idx in range(e-1, -1, -1):
            if num_list[idx] > num_list[idx+1]:
                num_list[idx], num_list[idx+1] = num_list[idx+1], num_list[idx]
            else:
                break

        print(*num_list)




N = int(input())
num_list = list(map(int, input().split()))
insert_sort(num_list)

