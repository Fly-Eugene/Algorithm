
bracket = list(input())
num_list = []
stack = []
check = True

for i in range(len(bracket)):
    # print('====================================')
    # print('현재 체크 중', bracket[i])

    if bracket[i] == '(' or bracket[i] == '[':
        stack.append(bracket[i])

    else:
        if stack:
            pop_item = stack.pop()
            num = 0
            while pop_item == '-' and stack:
                num += num_list.pop()
                pop_item = stack.pop()

            if bracket[i] == ')' and pop_item == '(':
                # print(') 닫는거 확인 중')
                if num == 0:
                    stack.append('-')
                    num_list.append(2)
                else:
                    stack.append('-')
                    num_list.append(num*2)

            elif bracket[i] == ']' and pop_item == '[':
                # print('] 닫는거 확인 중')
                if num == 0:
                    stack.append('-')
                    num_list.append(3)
                else:
                    stack.append('-')
                    num_list.append(num*3)

            else:
                check = False
                break
        else:
            check = False
            break

    # print('현재 stack', stack)
    # print('현재 num_list', num_list)

# print(num_list)
# print(stack)

if check == False or '(' in stack or '[' in stack:
    print(0)
else:
    print(sum(num_list))
