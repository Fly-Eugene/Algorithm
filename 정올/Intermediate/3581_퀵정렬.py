def quick_sort(left, right):
    if left < right:
        s = partition(left, right)
        quick_sort(left, s-1)
        quick_sort(s+1, right)


def partition(left, right):
    pivot = right
    i, j = left, right - 1

    while True:
        while arr[i] < arr[pivot] and i < right:
            i += 1
        while arr[j] > arr[pivot] and j > left:
            j -= 1

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    arr[pivot], arr[i] = arr[i], arr[pivot]
    print(*arr)
    return i





N = int(input())
arr = list(map(int, input().split()))
quick_sort(0, N-1)

