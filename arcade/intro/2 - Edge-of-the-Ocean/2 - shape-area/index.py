def shapeArea(n):
    if n == 0:
        area = 0;
    elif n == 1:
        area = 1
    else:
        area = (n * n) + ((n-1) * (n-1))
    return area


print(shapeArea(1))
print(shapeArea(2))
print(shapeArea(3))
print(shapeArea(5))


def shapeAreaV2(n):
    if n == 1:
        area = 1
    else:
        area = shapeAreaV2(n - 1) + (n - 1) * 4
    return area

def shapeAreaV3(n):
    return n * n + (n -1) * (n - 1)

print(shapeAreaV2(1))
print(shapeAreaV2(2))
print(shapeAreaV2(3))
print(shapeAreaV2(5))