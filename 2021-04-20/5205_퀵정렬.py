import sys
sys.stdin = open('sample_input (11).txt')

def quicksort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot-1)
        quicksort(arr, pivot+1, right)

def partition(arr, left, right):
    pivot = (left+right) // 2
    while left < right:
        while arr[left] < arr[pivot] and left < right:
            left += 1
        while arr[right] >= arr[pivot] and left < right:
            right -= 1
        if left < right:
            if left == pivot:
                pivot = right
            arr[left], arr[right] = arr[right], arr[left]
    arr[pivot], arr[right] = arr[right], arr[pivot]
    return right

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    left = 0
    right = N-1
    quicksort(A, left, right)
    print('#%d %d' %(tc, A[N//2]))

#### 교수님 풀이##
# def partition_l(a, l, r):
#     i = l-1                     # 피봇보다 큰 구간 왼쪽 경계
#     j = l                       # 피봇보다 큰 구간 오른쪽 경계
#     pivot = a[r]                # 가장 오른쪽 원소를 피봇으로 결정
#     for j in range(l, r):       # 피봇에 다다르기 전까지
#         if pivot >= a[j]:       # 피봇보다 작으면 i 이동
#             i += 1
#             a[i], a[j] = a[j], a[i]
#     a[i+1], a[r] = pivot, a[i+1] # 피봇과 교환
#     return i+1
#
# def partition_h(a, l, r):
#     pivot = a[l]
#     i = l
#     j = r
#     while i < j:
#         while i < r and a[i] <= pivot:
#             i += 1
#         while j > l and a[j] >= pivot:
#             j -= 1