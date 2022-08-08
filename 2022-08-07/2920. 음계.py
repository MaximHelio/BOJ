arr = list(map(int, input().split(' ')))
ascending = 0
descending = 0
mixed = 0
for i in range(0, len(arr)-1):
    if arr[i] < arr[i+1]: ascending += 1
    elif arr[i] > arr[i+1]: descending += 1
    else: mixed += 1

if ascending > 0 and descending == 0: print("ascending")
elif ascending ==0 and descending >0 : print("descending")
else: print("mixed")



a = list(map(int, input().split('')))
ascending = True
descending = True

for i in range(0, 7):
    if a[i] < a[i+1]: descending = False
    elif a[i] > a[i+1]: ascending = False

if ascending: print('ascending')
elif descending: print('descending')
else: print('mixed')

