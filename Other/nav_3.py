
## 문제번호를 idx로 해서 점수를 저장하는 배열을 만들어
## 푼 문제 idx를 저장하는 배열을 따로 만들어 1차로 걸러주기 위해

logs = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]
score_dict = {}
solved_dict = {} ## 학생별로 지금까지 푼 문제 idx 리스트를 저장
students = []
answer = set()

for log in logs:
    student, idx, score = log.split()
    idx, score = int(idx), int(score)

    if student not in students:  ## 학생 리스트 관리
        students.append(student)

    if student not in score_dict.keys(): ## 처음 채점되는 학생이면 세팅
        score_dict[student] = [0] * 101
        solved_dict[student] = [idx]

    else:
        if idx not in solved_dict[student]:
            solved_dict[student].append(idx)

    score_dict[student][idx] = score  ## 최근 score로 변경해주기


for i in range(len(students)):

    if students[i] not in answer and len(solved_dict[students[i]]) >= 5: ## 아직 의심자가 아니고, 푼 문제수가 5 이상일 때

        for j in range(i, len(students)):
            if solved_dict[students[i]].sort() == solved_dict[students[j]].sort(): ## 두 학생이 푼 문제의 번호가 같고
                if score_dict[students[i]] == score_dict[students[j]]: ## 푼 문제의 점수가 모두 같다면
                    ## 모든 조건을 충족함으로 asnwer에 추가한다.
                    answer.add(students[i])
                    answer.add(students[j])

    else: continue

answer = list(answer)
if len(answer) == 0:
    answer = ["None"]
else:
    answer.sort()

print(answer)














