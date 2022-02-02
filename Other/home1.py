from collections import defaultdict
temp = "a2c9b3c2z0"
temp2 = ''
res = ''

print(ord('a'))
print(ord('z'))

alpha_dict = {}
alpha_set = set()

for i in range(97, 123):
    alpha_dict[chr(i)] = 1
    alpha_set.add(chr(i))

arr = [0] * 26

left, right = 0, 0

while left < len(temp) and right < len(temp):
    print('======================================')
    print('현재 left가 알파벳', temp[left])

    if temp[left] not in temp2:
        temp2 += temp[left]
    right += 1

    num = ''
    while right < len(temp) and temp[right] not in alpha_set:
        print(left, '뒤로 숫자 체크 중', temp[right])
        num += temp[right]
        right += 1

    num = int(num)
    arr[ord(temp[left]) - 97] += num
    print('num은', num)

    left = right
    print('left 갱신', left)

print(temp2)
print(arr)

for i in range(len(temp2)):
    res += temp2[i] + str(arr[ord(temp2[i])-97])

print(res)
