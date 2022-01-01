from collections import deque


def bfs(stones, k, tmp):
    global answer, N

    queue = [(stones, tmp)]
    while queue:

        stones, tmp = queue.pop(0)

        for i in range(N):
            next = False
            new_stones = [0] * N

            for j in range(N):
                if i == j:
                    new_stones[j] = stones[i] + 1
                else:
                    if stones[j] == 0:
                        next = True
                        break
                    else:
                        new_stones[j] = stones[j] - 1

            if next == False:
                n_tmp = tmp + str(i)

                ## 정답일 경우
                if new_stones.count(0) == N-1 and sum(new_stones) == k:
                    if len(answer) > len(n_tmp):
                        answer = n_tmp
                    elif len(answer) == len(n_tmp) and answer < n_tmp:
                        answer = n_tmp

                ## 정답이 아닌 경우
                else:
                    if len(n_tmp) < len(answer):
                        queue.append((new_stones, n_tmp))




stones = [5, 7, 2, 4, 9]
N = len(stones)
k = 20
answer = str(12 ** 12)

bfs(stones, k, '')

if answer == str(12 ** 12):
    print(-1)
else:
    print(answer)





