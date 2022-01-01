
num_dict = { '####.##.##.####' : '0', '.#..#..#..#..#.' : '1', '###..#####..###' : '2', '###..####..####' : '3', '#.##.####..#..#' : '4',
             '####..###..####' : '5', '####..####.####' : '6', '###..#..#..#..#' : '7', '####.#####.####' : '8', '####.####..####' : '9'}

N = int(input())
signal = list(input())
arr = [[''] * (N//5) for _ in range(5)]
res = ''


# 시그널 그리기
for i in range(N):
    arr[i//(N//5)][(i%(N//5))] = signal[i]

# for i in range(5):
#     print(arr[i])

## 1이 맨 앞에 있는 경우
one = ''
for i in range(5):
    for j in range(2):
        one += arr[i][j]
if one == '#.#.#.#.#.':
    res += '1'

for s in range(N//5 - 2):
    tmp = ''
    for i in range(5):
        for j in range(s, s+3):
            tmp += arr[i][j]
    if tmp in num_dict.keys():
        res += num_dict[tmp]

## 끝에 1이 있는 경우
one = ''
for i in range(5):
    for j in range(N//5-2, N//5):
        one += arr[i][j]

if one == '.#.#.#.#.#':
    res += '1'

print(int(res))






