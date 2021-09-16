# 47분 시작, 26분 완료

print(ord('a'))  # 97
print(ord('z'))  # 122

research = ["xy","xy"]
n = 1
k = 1

# 1. 검색어 전처리하기
## 2차원 배열, index는 날짜(최대 31), 행은 각 알파벳 (97, 122)
arr = [[0] * 31 for _ in range(27)]

for i in range(len(research)):
    day = research[i]
    for alpha in day:
        num = ord(alpha) - 97
        arr[num][i] += 1


# n일 동안, 매일 최소 k번 이상 검색 && n일 동안의 검색량 총량이 2*n*k 이상이면 이슈 검색 ok
# 각 알파벳 별로 이슈 검색 횟수 cnt 하는 배열 만들기
issue = [0] * 27

for i in range(len(arr)):
    for j in range(len(arr[i])-n):
        chk_k = True
        chk_nk = 0

        for d in range(j, j+n):
            if arr[i][d] < k:
                chk_k = False
                break
            else:
                chk_nk += arr[i][d]

        if chk_k == True and chk_nk >= 2 * n * k:
            ## 이슈의 조건을 만족했다.
            issue[i] += 1

max_issue = max(issue)
if max_issue == 0:
    answer = None
    # print(answer)
else:
    answer_idx = issue.index(max_issue)
    answer = chr(answer_idx + 97)
    # print(answer)


