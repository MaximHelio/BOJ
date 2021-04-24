N = int(input())
lst = []
for _ in range(N):
    num = int(input())
    lst.append(num)
total = sum(lst)
# arithmetic mean
print(total//N)
# median
lst.sort()
if N % 2:
    print(lst[N//2])
print((lst[N//2]+lst[N//2-1])//2)
# Mode
lst_mode = [0] * N
for i in range(N):
    lst_mode[i] += lst.count(lst[i])
idx_set = set()
idx = lst_mode.index(max(lst_mode))
idx_set.add(lst[idx])
print(idx_set)
# range
print(max(lst) - min(lst))