
arr = [0, 1, 2, 2, 0, 0, 10, 3]
arr_cnt = [0] * (max(arr) + 1)
x = 3
max_MEX = 0

for num in arr:
    arr_cnt[num] += 1

while True:

    ## 현재 max_MEX 값과 동일한 num이 있는지 확인
    findMEX = False
    if arr_cnt[max_MEX] > 0:
        findMEX = True
        arr.remove(max_MEX)
        arr_cnt[max_MEX] -= 1
        max_MEX += 1

    # for i in range(len(arr)):
    #     if max_MEX == arr[i]:
    #         findMEX = True
    #         arr.pop(i)
    #         max_MEX += 1
    #         break

    ## max_MEX 값과 동일한 num이 없다면 / 연산으로 구할 수 있는 값을 찾는다
    if findMEX == False:
        for i in range(len(arr)):
            if (max_MEX - arr[i]) % x == 0:
                findMEX = True
                num = arr.pop(i)
                arr_cnt[num] -= 1
                max_MEX += 1
                break

    if findMEX == False:
        break

print(max_MEX)


