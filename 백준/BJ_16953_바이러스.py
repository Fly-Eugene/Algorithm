from collections import deque

def bfs():
    global A, B

    stack = deque()
    stack.append((A, 0))

    while stack:
        num, cnt = stack.popleft()
        num1, num2 = num*2, num*10 + 1

        n_cnt = cnt+1
        if num1 == B or num2 == B:
            return n_cnt + 1
        if num1 < B:
            stack.append((num1, n_cnt))
        if num2 < B:
            stack.append((num2, n_cnt))

    return -1



A, B = map(int, input().split())
res = bfs()
print(res)



