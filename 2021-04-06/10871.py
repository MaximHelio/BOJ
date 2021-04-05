N, X = map(int, input().split())
sequence = list(map(int, input().split()))
for num in sequence:
    if num < X:
        print(num, end=' ')