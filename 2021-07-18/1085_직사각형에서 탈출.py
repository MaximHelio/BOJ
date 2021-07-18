x, y, w, h = map(int, input().split())

min_value = min(abs(w-x), abs(x), abs(h-y), abs(y))
print(min_value)