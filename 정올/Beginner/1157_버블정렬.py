
def bubble_sort(num_list):

    for end in range(N-1, 0, -1):
        for j in range(end):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

        print(*num_list)


N = int(input())
num_list = list(map(int, input().split()))
bubble_sort(num_list)
