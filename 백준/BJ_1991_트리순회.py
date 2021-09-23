
def pre_tree(node):

    print(chr(node + 65), end = '')
    if arr[node][0] != -1:
        pre_tree(arr[node][0])
    if arr[node][1] != -1:
        pre_tree(arr[node][1])

def in_tree(node):

    if arr[node][0] != -1:
        in_tree(arr[node][0])

    print(chr(node + 65), end='')

    if arr[node][1] != -1:
        in_tree(arr[node][1])

def post_tree(node):
    if arr[node][0] != -1:
        post_tree(arr[node][0])
    if arr[node][1] != -1:
        post_tree(arr[node][1])

    print(chr(node + 65), end = '')

N = int(input())
arr = [[-1, -1] for _ in range(N)]

for _ in range(N):
    root, a, b = input().split()

    if a != '.':
        arr[ord(root) - 65][0] = ord(a) - 65

    if b != '.':
        arr[ord(root) - 65][1] = ord(b) - 65

pre_tree(0)
print()
in_tree(0)
print()
post_tree(0)


