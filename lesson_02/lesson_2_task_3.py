import math

def square(side):
    area = side * side
    return math.ceil(area)

side = float(input("Введите сторону квадрата: "))

result = square(side)

print(f"Площадь квадрата: {result}")
