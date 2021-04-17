word = input()
dials = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

ans = 0
for letter in word:
    for dial in dials:
        if(letter in dial):
            ans += dials.index(dial) + 3
print(ans)