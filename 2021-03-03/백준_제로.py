K = int(input())
lst = [int(input()) for _ in range(K)]
new_lst = []
for item in lst:
    if item: new_lst.append(item)
    else: new_lst.pop()
print(sum(new_lst))