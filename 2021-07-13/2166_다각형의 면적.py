N = int(input())
arr = []
for _ in range(N):
    xy = list(map(int, input().split()))
    arr.append(xy)
arr.append(arr[0])
a = 0
b= 0
for i in range(len(arr)-1):
    a += arr[i][0] * arr[i+1][1]
    b += arr[i+1][0] * arr[i][1]

area = 0.5*(abs(a-b))
print(area)