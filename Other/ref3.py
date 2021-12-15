
def findCurrentMinimum(sel):
    currentMinimum = 10 ** 18

    for i in range(len(sel) - 1):
        for j in range(i, len(sel)):
            diff = abs(sel[j] - sel[i])

            if diff < currentMinimum:
                currentMinimum = diff

    return currentMinimum


def comb(i, j, sel):
    global n, m, globalMaximum

    if i == m:
        print(sel)
        currentMinimum = findCurrentMinimum(sel)

        if currentMinimum > globalMaximum:
            globalMaximum = currentMinimum

    else:
        for k in range(j, n-m+i+1):
            sel[i] = arr[k]
            comb(i+1, k+1, sel)


arr = [1, 2, 3, 4]
n = len(arr)
m = 3

globalMaximum = 0

sel = [0] * m
comb(0, 0, sel)





