


stockPrices = [1, 2, 3, 3, 4, 5]
k = 3
n = len(stockPrices)

cnt = 0

profits = [0] * (n - k + 1)

for i in range(n - k + 1):
    increase = True

    if stockPrices[i + (k-1)] - stockPrices[i] < k - 1:
        increase = False

    else:
        ## 전월이 strictly high month일 경우
        if profits[i-1] == 1:
            diff = stockPrices[i + (k-2)] - stockPrices[i + (k-1)]
            if diff <= 0:
                increase = False
        else:
            for j in range(i, i + (k-1)):
                diff = stockPrices[j+1] - stockPrices[j]
                if diff <= 0:
                    increase = False
                    break

    if increase:
        print('지금 시작 월', i)
        profits[i] = 1
        cnt += 1


print(cnt)
