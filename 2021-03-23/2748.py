# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n = int(input())
arr = [0 for _ in range(n+1)]
arr[1] = 1

for i in range(2, n+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[-1])