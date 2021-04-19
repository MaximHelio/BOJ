num1, num2 = map(str, input().split())
reverse_num1 = num1[::-1]
reverse_num2 = num2[::-1]
print(max(reverse_num1, reverse_num2))
