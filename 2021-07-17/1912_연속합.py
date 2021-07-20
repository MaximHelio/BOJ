# D[i] : i번째 까지 연속합을 했을 때 최댓값. (이때, i번째 값을 반드시 사용한다)
# D[i] = max(D[i-1] + arr[i], arr[i])
# D[i] = D[i-2] + D[i-1]
input()
s = input()
arr_s = s.split()
arr = []
for i in arr_s: arr.append(int(i))
D = []
for i in range(len(arr)):
    m = arr[i]
    if i > 0 and D[i-1] > 0: m += D[i-1]
    D.append(m)
print(max(D))