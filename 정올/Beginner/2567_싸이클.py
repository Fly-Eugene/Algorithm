
def find_repeat(num):

    if (num * N) < P and num * N != 0:   # 이런 경우 싸이클에 포함되지 않는다.
        find_repeat(num * N)

    else:
        new_num = (num * N) % P

        if new_num in duple_set:
            return

        duple_set.add(new_num)
        find_repeat(new_num)



N, P = map(int, input().split())
duple_set = set()
find_repeat(N)

print(len(duple_set))


