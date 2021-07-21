T = int(input())
quo_types = [3, 2, 1]
for tc in range(1, T+1):
    n = int(input())
    cnt = 0
    for quo in quo_types:
        cnt += n // quo
        n %= quo
    print(cnt)