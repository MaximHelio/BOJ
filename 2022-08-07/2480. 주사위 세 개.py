arr = list(map(int, input().split()))
lst = []
for i in range(0, len(arr)):
    lst.append(arr[i])

slst = set(lst)

diff = len(lst) - len(slst)

if diff == 0: ans = max(lst) * 100

elif diff == 1: 
    for num in slst:
        if num in lst: lst.remove(num)
    ans = 1000 + lst[0] * 100

elif diff == 2: ans = max(slst) * 1000 + 10000

print(ans)