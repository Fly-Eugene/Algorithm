
while True:
    sentence = list(input().split())

    if sentence[0] == "END":
        break
    else:
        word = {}
        for w in sentence:
            if w in word:
                word[w] += 1
            else:
                word[w] = 1

        word_list = list(word.keys())
        word_list.sort()

        for w in word_list:
            print(w, ':', word[w])

