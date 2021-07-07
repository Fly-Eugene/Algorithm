
key_list = input()
sentence = input()

word_list = ['_'] * 200

s_idx = 65
for item in key_list:
    word_list[s_idx + 32] = item
    word_list[s_idx] = chr(ord(item) - 32)

    s_idx += 1

res = ''
for alpha in sentence:
    if alpha == ' ':
        res += ' '
    else:
        res += word_list[ord(alpha)]

print(res)

