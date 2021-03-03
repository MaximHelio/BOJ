S = str(input())
alphabet = []
ascii_a = ord("a")
ascii_z = ord("z")
for ascii in range(ord("a"), ord("z")+1):
    alphabet.append(chr(ascii))

for i in range(len(alphabet)):
    if alphabet[i] in S:
        alphabet[i] = S.find(alphabet[i])
    else: alphabet[i] = -1
print(*alphabet)