arr = list(map(int, input().split()))
for i in range(0, len(arr)):
    if arr[i] < arr[i+1]: continue
    