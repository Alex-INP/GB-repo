src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([i for i in src[1:] if i > src[src.index(i) - 1]])
