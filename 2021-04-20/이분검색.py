N, M = map(int, input().split())
arr = list(map(int, input().split()))
lt = 0
rt = N
mid = (lt+rt) // 2
if M == arr[mid]:
elif M < arr[mid]:
    rt = mid-1
elif M > arr[mid]:
    lt = mid+1
