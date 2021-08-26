
while True:
    n = int(input())

    if n == 0:
        break

    else:
        words = []
        upper_words = []
        for i in range(n):
            words.append(input())
            word = words[i].upper()  # 대문자로 만들기
            num = []  # ord 기록할 list
            for w in word:
                num.append(ord(w))

            upper_words.append([i, num])

        upper_words.sort(key=lambda x: x[1])

    fst_idx = upper_words[0][0]
    print(words[fst_idx])

