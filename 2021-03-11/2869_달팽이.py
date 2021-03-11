import math

A, B, V = map(int, input().split())

day = math.ceil((V-A)/(A-B)) + 1

print(day)

# while True:
#     cnt += 1
#     x += A
#     if x >= V: 
#         break
#     x -= B
# print(cnt)