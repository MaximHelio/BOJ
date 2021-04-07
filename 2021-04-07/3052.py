rem_list = []
for _ in range(10):
    num = int(input())
    rem = num % 42
    if rem not in rem_list:
        rem_list.append(rem)
print(len(rem_list))