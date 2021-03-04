import sys
sys.stdin = open("input (3).txt", "r")

R = int(input())
for rc in range(R):
    A = list(map(int, input().split())) # A가 내는 카드의 개수, A가 내는 카드에 대한 표현
    a_cnt4 = 0
    a_cnt3 = 0
    a_cnt2 = 0
    a_cnt1 = 0
    for num_a in A[1:]:
        if num_a == 4:
            a_cnt4 += 1
        if num_a == 3:
            a_cnt3 += 1
        if num_a == 2:
            a_cnt2 += 1
        if num_a == 1:
            a_cnt1 += 1

    B = list(map(int, input().split()))  # B가 내는 카드의 개수, B가 내는 카드에 대한 표현
    b_cnt4 = 0
    b_cnt3 = 0
    b_cnt2 = 0
    b_cnt1 = 0
    for num_b in B[1:]:
        if num_b == 4:
            b_cnt4 +=1
        if num_b == 3:
            b_cnt3 +=1
        if num_b == 2:
            b_cnt2 +=1
        if num_b == 1:
            b_cnt1 +=1

    if a_cnt4 > b_cnt4:
        print("A")
    elif a_cnt4 < b_cnt4:
        print("B")
    else:
        if a_cnt3 > b_cnt3:
            print("A")
        elif a_cnt3 < b_cnt3:
            print("B")
        else:
            if a_cnt2 > b_cnt2:
                print("A")
            elif a_cnt2 < b_cnt2:
                print("B")
            else:
                if a_cnt1 > b_cnt1:
                    print("A")
                elif a_cnt1 < b_cnt1:
                    print("B")
                else: print("D")