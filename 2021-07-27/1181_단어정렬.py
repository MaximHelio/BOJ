N = int(input())
word_dict = {}
for _ in range(N):
    word = str(input())
    word_dict[word] = len(word)
print(word_dict)
for i in range(N):
    for j in range(N-1):
        if word_dict[i]
