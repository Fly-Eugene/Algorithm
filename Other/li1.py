## 17분 소요

student = [0, 1, 0]
k = 2
N = len(student)
answer = 0

# 시작점 i
# 매번 cnt = 0으로 초기화
# 원하는 k 수를 만족하는 순간 cnt + 1
# 그리고서 뒤쪽으로 0이 나오면 cnt + 1
# 1 이 나오면 out

for i in range(N):
    cnt = 0
    now_k = 0
    for j in range(i, N):
        if now_k < k and student[j] == 0:
            continue
        elif now_k < k and student[j] == 1:
            now_k += 1
            if now_k == k:
                cnt += 1

        elif now_k == k and student[j] == 0:
            cnt += 1

        elif now_k == k and student[j] == 1:
            break

    answer += cnt

print(answer)
