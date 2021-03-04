N = int(input())
for _ in range(N):
    order = list(map(str, input().split()))
    queue = []
    cnt = 0
    if order[0] == "push":
        queue.append(int(order[1]))
        cnt += 1
    elif order[0] == "pop":
        if queue:
            print(queue.pop(0))
            cnt -= 1
        else: print(-1)
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        if queue: print(0)
        else: print(1)
    elif order[0] == "front":
        if queue:
            print(queue[0])
            cnt -= 1
        else: print(-1)
    elif order[0] == "back":
        if queue:
            print(queue[-1])
            cnt -= 1
        else: print(-1)