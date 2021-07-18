
def check(num):
    global Student

    need_st = 0
    for jew in jew_list:
        need_st += jew // mid
        if (jew % mid):
            need_st += 1

    # 해당 갯수로 학생들에게 나눠줄 때, 필요한 학생 수가 현재 학생 수보다 많다면 , return False
    if need_st > Student:
        return False
    else:
        return True



Student, M = map(int, input().split())
jew_list = [int(input()) for _ in range(M)]
total_jew = sum(jew_list)

min_jew = 1
max_jew = max(jew_list)
res = max_jew

while min_jew <= max_jew:
    mid = (min_jew + max_jew) // 2

    if check(mid):
        # print('현재 나눠주는 갯수', mid, '결과 값', check(mid))
        res = min(res, mid)
        max_jew = mid - 1

    else:
        # print('현재 나눠주는 갯수', mid, '결과 값', check(mid))
        min_jew = mid + 1

print(res)



