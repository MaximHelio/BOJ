N = int(input()) # 시험 본 과목의 수
score_list = list(map(int, input().split()))
score_max = max(score_list)
new_sum = 0
for score in score_list:
    new_score = (score / score_max) * 100
    new_sum += new_score
new_average = new_sum / N
print(new_average)