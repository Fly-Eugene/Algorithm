
N = int(input())
num_list = list(map(int, input().split()))

stack = []
result = [-1] * N

for idx in range(N):
    if stack and num_list[stack[-1]] < num_list[idx]:
        while stack and num_list[stack[-1]] < num_list[idx]:
            find_bigger = stack.pop()
            result[find_bigger] = num_list[idx]
        stack.append(idx)

    else:
        stack.append(idx)

print(*result)