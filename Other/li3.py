
## 39분 생각 시작,

# 분류 번호 별로 밀린 작업 번호 저장
# 이걸로 중요도와 걸리는 시간을 계산 가능

jobs = [[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]
temp = [[] for _ in range(101)]
answer = []

## 우선 어느 초에 일이 들어오는지 표시한다.
jobs_income = [-1] *  1000000
for i in range(len(jobs)):
    sec = jobs[i][0]
    jobs_income[sec] = i

# working_time 과 now_idx 를 저장하고 있는다.
# working_time이 끝난 타임을 따로 표시해야된다. => -1초씩 줄여나가기 => working_time이 0이 됐을 때 밑의 판단 2가지 실행
# 1. 해당 시간에 새로 받아진 요청을 파악한다. => 같은 idx 이면 이어서 작업한다. => 아니면 대기열에 추가한다.
# 2. 대기열의 중요도를 계산해서 가장 중요도 높은 idx 찾기 => 작업 시간을 합해서 working_time 으로 등록

now_time = 0
working_time = 0
now_idx = -1
stop = 1

while stop:
    if working_time == 0:
        ## 처음 시작하는 일을 찾는다.
        if now_idx == -1:
            if jobs_income[now_time] != -1:
                print('일을 찾았다', now_time)
                working_time += jobs[jobs_income[now_time]][1]
                now_idx = jobs[jobs_income[now_time]][2]
                answer.append(now_idx)
                print('일 찾고 나서 working time', working_time)

            else:
                print('일을 아직 찾지 못했다', now_time)
                now_time += 1
                continue

        ## 이미 작업은 시작한 상황
        else:
            ## 일이 끝났고, 해당 시간에 들어온 일이 있다.
            if jobs_income[now_time] != -1:
                chk_idx = jobs[jobs_income[now_time]][2]

                if now_idx == chk_idx:  # 같은 종류의 일이 들어오면 이어서 일한다.
                    working_time += jobs[jobs_income[now_time]][1]
                else:  # 다른 종류의 일이 들어오면 우선 temp에 넣는다.
                    temp[chk_idx].append(jobs_income[now_time])

            ## 일이 끝났고, 해당 시간에 들어온 일이 없다.
            ## 대기 중인 일 중에 찾는다.
            else:
                max_imp = 0
                max_idx = -1
                for i in range(len(temp)):
                    ## 각 종류의 일마다 중요도를 계산한다.
                    now_imp = 0
                    for t in temp[i]:
                        now_imp += jobs[t][3]

                    ## 중요도 값을 갱신한다.
                    if max_imp < now_imp:
                        max_imp = now_imp
                        max_idx = i

                if max_idx == -1:
                    stop = 0
                    # return answer
                else:
                    for tmp_item in temp[max_idx]:
                        working_time += jobs[tmp_item][1]

                    now_idx = max_idx
                    answer.append(max_idx)

    else:   ## 작업 중에 다른 요청들이 들어오면
        if jobs_income[now_time] != -1:
            chk_idx = jobs[jobs_income[now_time]][2]
            if now_idx == chk_idx:
                working_time += jobs[jobs_income[now_time]][1]
            else:
                temp[chk_idx].append(jobs_income[now_time])

    now_time += 1
    working_time -= 1




print(answer)


