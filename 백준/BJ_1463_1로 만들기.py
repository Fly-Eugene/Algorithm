
N = int(input())

if N == 1:
    print(0)
else:
    count_min = [0] * (N+1)
    count_min[2] = 1

    for i in range(3, N+1):
        if i % 2 == 0:
            count_min[i] = min(count_min[i//2] + 1, count_min[i-1] + 1)

        if i % 3 == 0:
            temp = min(count_min[i//3] + 1, count_min[i-1] + 1)
            if count_min[i] and count_min[i] < temp:
                continue
            count_min[i] = temp

        elif i % 2 and i % 3:
            # print(i)
            count_min[i] = count_min[i-1] + 1

    print(count_min[N])

