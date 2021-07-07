
def row(r, c, color):
    if 0 <= c-1 < 19:
        if arr[r][c-1] == color: return 0
    for i in range(4):
        c += 1
        if 0 <= c < 19:
            if arr[r][c] != color:
                return 0
        else: return 0

    c += 1
    if c == 19:
        return (1, 1)
    elif 0 <= c < 19:
        if arr[r][c] != color:
            return (1, 1)
        else: return 0

def col(r, c, color):
    if 0 <= r-1 < 19:
        if arr[r-1][c] == color: return 0
    for i in range(4):
        r += 1
        if 0 <= r < 19:
            if arr[r][c] != color:
                return 0
        else: return 0

    r += 1
    if r == 19:
        return (1, 2)
    elif 0 <= c < 19:
        if arr[r][c] != color:
            return (1, 2)
        else:
            return 0

def cross_1(r, c, color):
    if 0 <= r-1 < 19 and 0 <= c-1 < 19:
        if arr[r-1][c-1] == color: return 0
    for i in range(4):
        r += 1
        c += 1
        if 0 <= r < 19 and 0 <= c < 19:
            if arr[r][c] != color:
                return 0
        else: return 0

    r += 1
    c += 1
    if r == 19 or c == 19:
        return (1, 3)
    elif 0 <= r < 19 and 0 <= c < 19:
        if arr[r][c] != color:
            return (1, 3)
        else:
            return 0

def cross_2(r, c, color):
    if 0 <= r-1 < 19 and 0 <= c+1 < 19:
        if arr[r-1][c+1] == color: return 0
    for i in range(4):
        r += 1
        c -= 1
        if 0 <= r < 19 and 0 <= c < 19:
            if arr[r][c] != color:
                return 0
        else: return 0

    r += 1
    c -= 1
    if r == 19 or c == 19:
        return (1, 4)
    elif 0 <= r < 19 and  0 <= c < 19:
        if arr[r][c] != color:
            return (1, 4)
        else: return 0



arr = [list(map(int, input().split())) for _ in range(19)]
res = 0
dir = 0
stop = 0


for i in range(19):
    if arr[i].count(1) or arr[i].count(2):
        for j in range(19):
            if arr[i][j] != 0:
                res = row(i, j, arr[i][j])
                if res == 0:
                    res = col(i, j, arr[i][j])
                    if res == 0:
                        res = cross_1(i, j, arr[i][j])
                        if res == 0:
                            res = cross_2(i, j, arr[i][j])

            if res != 0:
                stop = 1
                if res[1] != 4:
                    print(arr[i][j])
                    print(i+1, j+1)
                    break
                else:
                    print(arr[i][j])
                    print(i+5, j-3)
                    break

    else:
        continue

    if stop == 1:
        break

if stop == 0:
    print(0)
