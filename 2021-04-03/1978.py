N = int(input())
tup = map(int, input().split())
prime = []
for num in tup:
    quo_list = []
    for quo in range(1, num):
        if num % quo == 0: quo_list.append(quo)
    if len(quo_list) == 1: prime.append(num)
print(len(prime))