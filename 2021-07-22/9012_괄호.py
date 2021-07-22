T = int(input())
for _ in range(T):
     sentence = str(input())
     stack = []
     for i in range(len(sentence)):
         if sentence[i] == '(':
             stack.append(sentence[i])
         elif sentence[i] == ')':
             if len(stack):
                 stack.pop()
             else:
                print("NO")
                break

     # 조합과정 마치고 난 후
     if len(stack) == 0: result = "YES"
     else: result = "NO"
     print(result)


