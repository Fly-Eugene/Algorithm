
while True:
    num = input()
    if int(num):
        N = len(num)
        new_num = [0]*N
        res = 0

        for i in range(N//2):
            new_num[i] = num[N-i-1]
            new_num[N-i-1] = num[i]
            res += int(num[N-i-1]) + int(num[i])

        if N % 2:
            new_num[N//2] = num[N//2]
            res += int(num[N//2])

        num_res = ''.join(new_num)
        print(int(num_res), end = ' ')
        print(res)

    else:
        break