
def calc_diff(start, end):
    hour_s, min_s = start.split(':')
    hour_e, min_e = end.split(':')
    s_time = int(hour_s) * 60 + int(min_s)
    e_time = int(hour_e) * 60 + int(min_e)

    time_diff = e_time - s_time
    return time_diff

def calc_charge(time, fees):
    res = 0
    if time <= fees[0]:
        res += fees[1]

    elif time > fees[0]:
        res += fees[1]
        time -= fees[0]
        share = time // fees[2]
        rest = time % fees[2]

        if rest:  # 올림처리
            share += 1
        res += share * fees[3]

    return res



fees = [180, 5000, 10, 600]
records =  ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

cars = []  ## 차량들 번호만 저장하는 배열
last_time = [] ## 각 차량들의 마지막 IN 시간 기록, OUT 된 경우는 IN 내용을 제거한다.
time_sum = [] ## 각 차량들의 누적 시간을 기록하는 배열

for i in range(len(records)):
    time, car_num, inout = records[i].split()

    # 새로 들어온 차량일 경우
    if car_num not in cars:
        cars.append(car_num)
        last_time.append([])
        time_sum.append(0)

    car_idx = cars.index(car_num)
    if inout == 'IN':
        last_time[car_idx].append(time)

    elif inout == 'OUT':
        # 시간 차 계산
        in_time = last_time[car_idx].pop()
        time_diff = calc_diff(in_time, time)
        time_sum[car_idx] += time_diff


## 마지막에 출차 내역이 없는 경우 23:59 분에 나간 것으로 간주
for i in range(len(last_time)):
    if last_time[i]:
        in_time = last_time[i].pop()
        time = "23:59"
        time_diff = calc_diff(in_time, time)
        time_sum[i] += time_diff

cars_sort = sorted(cars)
answer = []
for car in cars_sort:
    car_idx = cars.index(car)
    charge = calc_charge(time_sum[car_idx], fees)
    answer.append(charge)



