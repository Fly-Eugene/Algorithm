


#
# id_dict = {"A" : 1, "B" : 1}
# for i in id_dict.keys():  ## A B
#     print(i)
#
# print("A" in id_dict.keys())
# id_dict["C"] = 1
#
# print(id_dict)


id_list = ["A B C D", "A D", "A B D", "B D"]
k = 2
id_dict = {}
answer = 0

for day in id_list:
    day_list = list(day.split())
    day_list.sort()

    ## 하루에 1장이상은 안됨
    for i in range(len(day_list)):
        if i == 0:
            if day_list[i] in id_dict.keys(): ## 한번이라도 쿠폰을 받은 회원이라면
                if id_dict[day_list[i]] < k:  ## 아직 받은 전체 쿠폰 수가 k개 미만이면
                    id_dict[day_list[i]] += 1
                    answer += 1
                else: continue
            else:
                id_dict[day_list[i]] = 1
                answer += 1

        else:
            if day_list[i-1] != day_list[i]:  ## 이전 고객과 같으면 하루 1장이상 지금 X
                if day_list[i] in id_dict.keys():
                    if id_dict[day_list[i]] < k:
                        id_dict[day_list[i]] += 1
                        answer += 1
                    else: continue
                else:
                    id_dict[day_list[i]] = 1
                    answer += 1


print(answer)








