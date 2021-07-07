
def make_paskal(n):
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                paskal[i][j] = 1
            else:
                paskal[i][j] = paskal[i-1][j-1] + paskal[i-1][j]



n, m = map(int, input().split())
paskal = [[0] * n for _ in range(n)]

make_paskal(n)

if m == 1:
    for i in range(n):
        res = paskal[i][:i+1]
        print(*res)

elif m == 2:
    for i in range(n):
        res = paskal[n-i-1][:n-i]
        print(' ' * i, end = '')
        print(*res)

else:
    for j in range(n-1, -1, -1):
        res = []
        for i in range(n-1, j-1, -1):
            res.append(paskal[i][j])

        print(*res)

