N = int(input())
a= N // 5 # five_max_limit
b = N // 3 # three_max_limit
for i in range(a, -1, -1):
    if (N - i * 5) % 3:
        print('-1')
    else:
