
n = int(input())

for j in range(n):
    for i in range(n):
        if i % 2 == 0:
            num = i*n + j + 65
            while num < 65 or num > 90:
                if num > 90:
                    num -= 26
                elif num < 65:
                    num += 26
            print(chr(num), end = ' ')

        else:
            num = (i+1)*n - (j+1) + 65
            while num < 65 or num > 90:
                if num > 90:
                    num -= 26
                elif num < 65:
                    num += 26
            print(chr(num), end = ' ')
    print()