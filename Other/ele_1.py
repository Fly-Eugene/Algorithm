def quicksort(left, right):

    if left < right:
        s = partition(left, right)
        quicksort(left, s-1)
        quicksort(s+1, right)

def partition(left, right):

    pivot = left
    i, j = left+1, right

    while True:
        while A[i] < A[pivot] and i < right:
            i += 1
        while A[j] > A[pivot] and left < j:
            j -= 1
        if j <= i:
            break
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1

    A[pivot], A[j] = A[j], A[pivot]
    return j


A = [7, 4, 2, 5, 3, 9, 6, 8]
odd_max, even_max = 0, 0

quicksort(0, len(A)-1)

for i in range(len(A)-1, -1, -1):
    ## 홀수일 경우
    if A[i] % 2 and odd_max == 0:
        odd_max = A[i]

    ## 짝수일 경우
    elif A[i] % 2 == 0 and even_max == 0:
        even_max = A[i]

    if even_max and odd_max:
        break

res = odd_max + even_max
print(A)
print(even_max, odd_max)
