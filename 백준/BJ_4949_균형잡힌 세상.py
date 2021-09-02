
def check(sentence):
    stack = []
    for i in range(len(sentence)):
        if sentence[i] == '[' or sentence[i] == '(':
            stack.append(sentence[i])
        elif sentence[i] == ']':
            if stack == []:
                return False
            elif stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif sentence[i] == ')':
            if stack == []:
                return False
            elif stack[-1] == '(':
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

while True:
    sentence = list(input())
    if sentence[0] == '.':
        break
    else:
        if check(sentence):
            print("yes")
        else:
            print("no")
