import sys
sys.stdin = open("input (4).txt", "r")

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    s1_x = set([i for i in range(x1, p1+1)]) # 3~50
    s2_x = set([i for i in range(x2, p2+1)]) # 10~60
    s1_y = set([i for i in range(y1, q1+1)]) # 100~200
    s2_y = set([i for i in range(y2, q2+1)]) # 100~300

    x_common = s1_x & s2_x
    y_common = s1_y & s2_y

    if len(x_common) > 1 and len(y_common) > 1:
        print("a") # 직사각형
    elif len(x_common) == 1 and len(y_common) == 1:
        print("c") # 점
    elif len(x_common) == 0 and len(y_common) == 0:
        print("d") # 공통 부분이 없음
    elif (len(x_common) > 1 and len(y_common)== 1) or (len(x_common)== 1 and len(y_common) > 1):
        print("b") # 선분

