elements = (-20, -5, 10, -1, 30)
result = []
if len(elements) > 0:
    result = sorted(elements, key=abs)
print(result)
