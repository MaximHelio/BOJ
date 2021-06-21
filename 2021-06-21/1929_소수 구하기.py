# M이상 N 이하의 소수를 모두 출력
# 3, 16
M, N = map(int, input().split())
arr = []
# 한 줄에 하나씩 증가하는 순서대로 소수를 출력한다
# 3, 5, 7, 11, 13
for i in range(1, N):
    if i == 1:
        pass
    elif i == 2:
        arr.append(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i-1:
                arr.append(i)
for i in arr:
    print(i)