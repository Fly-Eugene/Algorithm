
# 65~90 대문자

n = int(input())

for j in range(n-1, -1, -1):
    for i in range(n, 0, -1):
        num = n* (i-1) + j + 65

        while num > 90 or num < 65:
            if num > 90:
                num -= 26
            elif num < 65:
                num += 26
        print(chr(num), end =' ')

    print()
