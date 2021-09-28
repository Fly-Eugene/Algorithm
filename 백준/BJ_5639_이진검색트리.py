import sys
sys.setrecursionlimit(10 ** 9)

def post_order(st, end):
    if st > end:
        return

    else:
        div = end + 1
        for i in range(st+1, end+1):
            if node[st] < node[i]:
                div = i
                break

        # 왼쪽 트리
        post_order(st + 1, div - 1)
        # 오른쪽 트리
        post_order(div, end)
        print(node[st])


cnt = 0
node = []
while True:
    try:
        n = int(input())
        node.append(n)
        cnt += 1
    except:
        break

post_order(0, cnt-1)


