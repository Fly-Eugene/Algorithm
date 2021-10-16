def check_weekend(num, day):
    day_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    remain = (num-1) % 7

    day_idx = day_list.index(day)
    new_day_idx = (day_idx + remain) % 7

    new_day = day_list[new_day_idx]
    if new_day in ("SAT", "SUN"):
        return True
    else:
        return False


def calc_holiday(start_num, day, leave, holidays):

    holiday_len = 0
    num = start_num

    while num <= 30:
        if check_weekend(num, day):
            # print(num, '지금 주말이야')
            holiday_len += 1
        elif num in holidays:
            # print(num, '지금 연휴야')
            holiday_len += 1
        else:
            if leave > 0:
                leave -= 1
                # print('연차 씀', leave)
                holiday_len += 1
            else:
                # print('더 이상 연차를 쓸 수 없어', holiday_len)
                return holiday_len
        num += 1
    else:
        # print('30일 이상이면 갈 수 없어', holiday_len)
        return holiday_len



answer = -1
leave = 4
day = 'FRI'
holidays = [6, 21, 23, 27, 28]

for i in range(1, 31):
    holiday_len = calc_holiday(i, day, leave, holidays)
    if answer < holiday_len:
        answer = holiday_len

print(answer)









