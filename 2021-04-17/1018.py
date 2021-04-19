# N, M = map(int, input().split())
# data = [list(input()) for _ in range(N)]
#
# # correct 8*8 chess array
# arr_w = [[0]* 8 for _ in range(8)]
# arr_b = [[0]* 8 for _ in range(8)]
# for row in range(8):
#     for col in range(8):
#         # arr_w
#         if row % 2 == col % 2:
#             arr_w[row][col] = 'W'
#         else:
#             arr_w[row][col] = 'B'
#         # arr_b
#         if row % 2 == col % 2:
#             arr_b[row][col] = 'B'
#         else:
#             arr_b[row][col] = 'W'
#
# cnt_w = 0
# cnt_b = 0
# for i in range(N-8):
#     for j in range(M-8):
#         if data[i][j] != arr_w[i][j]: cnt_w += 1
#
# for i in range(N):
#     for j in range(M):
#         if data[i][j] != arr_b[i][j]: cnt_b += 1
#
# print(cnt_w)
# print(cnt_b)
def check_BW(matrix):
    case1_not_match = 0
    case2_not_match = 0

    # case 1 시작점(0,0)이 W 인경우
    for x in range(8):
        for y in range(8):
            if ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 == 1) and (y % 2 == 1)):  # 행짝 열짝, 행홀 열홀
                if matrix[x][y] != "W":
                    case1_not_match += 1

            elif ((x % 2 == 1) and (y % 2 == 0) or (x % 2 == 0) and (y % 2 == 1)):  # 행홀 열짝, 행짝 열홀
                if matrix[x][y] != "B":
                    case1_not_match += 1

    # case 2 시작점(0,0)이 B 인경우
    for x in range(8):
        for y in range(8):
            if ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 == 1) and (y % 2 == 1)):  # 행짝 열짝, 행홀 열홀
                if matrix[x][y] != "B":
                    case2_not_match += 1

            elif ((x % 2 == 1) and (y % 2 == 0) or (x % 2 == 0) and (y % 2 == 1)):  # 행홀 열짝, 행짝 열홀
                if matrix[x][y] != "W":
                    case2_not_match += 1

    return min(case1_not_match, case2_not_match)


def solution():
    input_list = []
    M, N = map(int, sys.stdin.readline().split())
    for idx in range(M):
        input_list.append([i for i in sys.stdin.readline()][:-1])

    min_revise_cnt = 123041234723842
    for row in range(M - 7):
        for col in range(N - 7):
            # 8*8 매트릭스로 자르기
            slice_mat = [one_row[col:col + 8] for one_row in input_list[row:row + 8]]
            revise_cnt = check_BW(slice_mat)
            min_revise_cnt = min(min_revise_cnt, revise_cnt)

    return min_revise_cnt


print(solution())