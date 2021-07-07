
pipes = list(input())
N = len(pipes)

pipe_cnt, all_cnt = 0, 0
for i in range(N-1):
    if pipes[i] == '(' and pipes[i+1] != ')':
        pipe_cnt += 1
        all_cnt += 1
    elif pipes[i] == '(' and pipes[i+1] == ')':
        all_cnt += pipe_cnt
        continue
    elif pipes[i] == ')' and pipes[i-1] != '(':
        pipe_cnt -= 1

print(all_cnt)

