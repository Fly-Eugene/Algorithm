
def check(palin):

    left, right = 0, len(palin)-1

    while left < right:
        if palin[left] == palin[right]:
            left +=1
            right -= 1
        else:
            res1 = doubleCheck(left + 1, right, palin)
            res2 = doubleCheck(left, right-1, palin)

            if res1 or res2:
                return 1
            else:
                return 2

    return 0

def doubleCheck(left, right, palin):

    while left < right:
        if palin[left] == palin[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


N = int(input())

for n in range(N):
    palin = input()
    res = check(palin)

    print(res)
