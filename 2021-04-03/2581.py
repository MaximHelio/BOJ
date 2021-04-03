M = int(input())
N = int(input())
num_list = []
for i in range(M, N+1):
    num_list.append(i)
prime = []
for j in num_list:
    quo_list = []
    for quo in (2, j):
        if j % quo == 0: quo_list.append(quo)
    if len(quo_list) == 0:
        prime.append(j)
print(prime)