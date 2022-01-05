import math

def find_one(n, k):
    global N

    if len(answer) == N-1:
        answer.append(numbers[-1])
        return
    else:
        numberOfCases = math.factorial(n) // n
        sequence = math.ceil(k / numberOfCases)
        answer.append(numbers.pop(sequence))

        find_one(n-1, k-(numberOfCases*(sequence-1)))

def find_k(tmp):
    global N

    for num in tmp:
        numberOfCases = math.factorial(N) // N
        idx = numbers.index(num)
        if len(numbers) == 2:
            idx += 1
            answer.append(numberOfCases*idx)
            return
        numbers.pop(idx)
        answer.append(numberOfCases*idx)
        N -= 1




N = int(input())
tmp = list(map(int, input().split()))
order = tmp.pop(0)

if order == 1:
    k = tmp[0]
    numbers = [i for i in range(N+1)]
    answer = []
    find_one(N, k)
    print(*answer)

else:
    k = tmp
    numbers = [i for i in range(1, N+1)]
    answer = []
    find_k(tmp)
    print(sum(answer))


