
## 첫번째 문자열에 두번째 문자열의 순서를 기록한다.
word_a = list(input())
word_b = list(input())

number_a = [[] for _ in range(len(word_a))]
memo = [0] * len(word_a)

for i in range(len(word_b)):
    w = word_b[i]
    for j in range(len(word_a)):
        if w == word_a[j]:
            number_a[j].append(i)

for i in range(len(memo)):
    now_idx = max(number_a[i])
    max_idx = -1
    cnt = 0
    for j in range(i):
        continue






print(number_a)







