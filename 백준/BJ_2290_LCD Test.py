
num_dict = {'0' : [1, 0, 1, 1, 1, 1, 1], '1' : [0, 0, 0, 0, 1, 0, 1], '2' : [1, 1, 1, 0, 1, 1, 0], '3' : [1, 1, 1, 0, 1, 0, 1], '4' : [0, 1, 0, 1, 1, 0, 1], '5' : [1, 1, 1, 1, 0, 0, 1],
            '6' : [1, 1, 1, 1, 0, 1, 1], '7' : [1, 0, 0, 0, 1, 0, 1], '8' : [1, 1, 1, 1, 1, 1, 1], '9' : [1, 1, 1, 1, 1, 0, 1]}

s, n = map(int, input().split())
n = str(n)
res = ['' for _ in range((2 * s + 3))]

for num in n:
    arr = [[' '] * (s + 2) for _ in range(2 * s + 3)]
    display = num_dict[num]

    # print('현재 num은?', num)
    for i in range(1, s+1):

        if display[0]:
            arr[0][i] = '-'
        if display[1]:
            arr[s+1][i] = '-'
        if display[2]:
            arr[2*s + 2][i] = '-'
        if display[3]:
            arr[i][0] = '|'
        if display[4]:
            arr[i][s+1] = '|'
        if display[5]:
            arr[s+1+i][0] = '|'
        if display[6]:
            arr[s+1+i][s+1] = '|'

    for i in range(2*s + 3):
        res[i] += ''.join(arr[i]) + ' '


for i in range(2 * s + 3):
    print(res[i])


