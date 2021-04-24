import sys
sys.stdin = open('sample_input (12).txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    answer = 0
    for b in B:
        # 중간을 탐색하기 때문에 최소점과 최대점을 잡아준다.
        min_idx = 0
        max_idx = N - 1
        # 왼쪽으로 갔는지 오른쪽으로 갔는지 체크하기 위한 용도
        flag = 0
        # 탐색범위가 같아지거나 엇갈릴때까지 반복한다.
        while min_idx <= max_idx:
            # 중간지점의 위치를 구한다.
            mid_idx = (min_idx + max_idx) // 2
            # 중간지점의 값이 정답이라면 answer를 늘리고 반복문을 중지한다.
            if A[mid_idx] == b:
                answer += 1
                break
            # 선택한 인덱스 값이 찾는값보다 크다면
            elif A[mid_idx] > b:
                # 선택한 인덱스 위쪽은 필요없으므로 최대 인덱스 위치를 수정한다.
                max_idx = mid_idx - 1
                # 이전에도 왼쪽을 선택했다면 중지
                if flag == 1: break
                # 왼쪽으로 갔다고 표시한다.
                flag = 1
            else:
                min_idx = mid_idx + 1
                if flag == -1: break
                flag = -1
    print('#%d %d' %(tc, answer))

# ## 교수님 풀이 ##
# def binaryS(l, r, key):
#     if l > r:
#         return 0
#
#     m = (l+r) // 2
#     if lst[m] == key:
#         return 1
#     elif lst[m] < key:
#         if d == 1:
#             return 0
#         d = 1
#         t = binaryS(m+1, r, key)
#         return t
#     else:
#         if d == 0:
#             return 0
#         d = 0
#         t = binaryS(l, m-1, key)
#         return t
#
# d = -1            #left=0, right=1