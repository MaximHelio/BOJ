N = int(input())
arr = []
for _ in range(1, N+1):
    num = int(input())
    arr.append(num)

for i in range(len(arr)):
    if i == 0 and arr[0] == 0:
        ans = 0
        print(ans)
    elif i > 0 and arr[i] == 0:
        ans = max(arr[:i])
        print(ans)
        arr.pop(max(arr[:i]))