def find_pair(num):
    global min_sum, pair
    left, right = 0, N-1

    while left <= right:
        mid = (left + right) // 2

        # 나와 pair를 할 수 없다. 즉 수치가 똑같은 용액과 pair를 지어줄 수 없다.
        if num == liquid_list[mid]:
            if mid == 0 or mid == N-1:
                break
            if abs(num + liquid_list[mid-1]) <= abs(num + liquid_list[mid+1]):
                right = mid - 1
            else:
                left = mid + 1

        else:
            if abs(liquid_list[mid] + num) < abs(min_sum):
                min_sum = liquid_list[mid] + num
                pair = [liquid_list[mid], num]

                if min_sum == 0:   ## 최소 합이 0 이라면 바로 break 하기
                    break

            if liquid_list[mid] + num < 0:
                left = mid + 1

            else:
                right = mid - 1



N = int(input())
liquid_list = list(map(int, input().split()))

liquid_list.sort()

min_sum = 2000000000
pair = [0, 0]

for num in liquid_list:
    find_pair(num)

    if min_sum == 0:
        break

pair.sort()
print(*pair)
