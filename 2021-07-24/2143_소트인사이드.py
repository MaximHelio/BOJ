inp = str(input())
arr = []
for i in range(len(inp)):
    arr.append(int(inp[i]))
arr.sort(reverse=True)
res = str()
for j in range(len(arr)):
    res = res + str(arr[j])
print(res)