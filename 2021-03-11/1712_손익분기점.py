A, B, C = map(int, input().split())
# A: 고정비용, B: 가변비용= 재료비+ 인건비, C: 노트북 가격
# x: 판매 대수 

if B >= C: print(-1)
else:
    print(A // (C - B) + 1)
