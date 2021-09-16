
## k번 이상 신고 당한 user 찾기
## 해당 user을 신고한 user은 이메일 전송 받음


id_list = ["muzi", "frodo", "apeach", "neo"]
N = len(id_list)
k = 2
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
send = [[] for _ in range(N) ]  # 각 캐릭터에게 경고를 보낸 사람 리스트를 저장
take = [0] * N  # 각 캐릭터가 받은 경고 횟수

answer = [0] * N

for i in range(len(report)):
    a, b = report[i].split()
    a_idx = id_list.index(a)
    b_idx = id_list.index(b)

    if a in send[b_idx]:
        continue
    else:
        send[b_idx].append(a)
        take[b_idx] += 1

for i in range(N):
    if take[i] >= k:
        for who in send[i]:
            who_idx = id_list.index(who)
            answer[who_idx] += 1

print(answer)











