
def bi(num):
    res = ''
    while num > 0:
        res = str(num % 2) + res
        num = num // 2

    return res

def ox(num):
    res = ''
    while num > 0:
        res = str(num % 8) + res
        num = num // 8

    return res

def hex(num):
    res = ''
    while num > 0:
        if num % 16 < 10:
            res = str(num % 16) + res
        else:
            res = chr(num % 16 + 55) + res

        num = num // 16

    return res

n, b = map(int, input().split())
res = 0

if b == 2:
    res = bi(n)
elif b == 8:
    res = ox(n)
elif b == 16:
    res = hex(n)

print(res)
