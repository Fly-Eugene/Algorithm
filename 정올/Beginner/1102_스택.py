
N = int(input())
stack = []

for n in range(N):
    command = list(input().split())

    if command[0] == 'i':
        stack.append(command[1])
    elif command[0] == 'o':
        if len(stack) == 0:
            print('empty')
        else:
            print(stack.pop())
    else:
        print(len(stack))