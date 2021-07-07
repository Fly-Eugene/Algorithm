
def quickSort(arr, left, right):
    if left < right:
        start = partition(arr, left, right)
        quickSort(arr, left, start-1)
        quickSort(arr, start+1, right)

def partition(arr, pivot, right):
    x= arr[right]
    i = pivot - 1

    for j in range(pivot, right):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1




T = int(input())

for tc in range(T):
    num_list = list(map(int, input().split()))

    ## quick sort (Lomuto partition 알고리즘)
    quickSort(num_list, 0, len(num_list)-1)
    print(num_list[-3])




