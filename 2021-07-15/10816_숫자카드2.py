import sys

input = sys.stdin.readline

N = int(input())
card_nums = list(map(int, input().split()))

M = int(input())
target_list = list(map(int, input().split()))

dicts = {}

for check_num in card_nums:
    if (check_num in dicts):
        dicts[check_num] += 1
    else:
        dicts[check_num] = 1

# ' '을 사이에 두고 반복하는 문자를 붙임
print(' '.join(str(dicts[target]) if target in dicts else '0' for target in target_list))