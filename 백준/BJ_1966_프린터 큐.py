
T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    numbers = [i for i in range(N)]
    order_list = []

    while arr:

        priority = arr[0]
        max_num = max(arr)
        item = arr.pop(0)
        num = numbers.pop(0)

        if max_num == priority:
            order_list.append(num)
        else:
            arr.append(item)
            numbers.append(num)

    # print(order_list)
    print(order_list.index(M) + 1)






