def is_even(number):
    return number % 2 == 0


def calculate_area(length, width):
    return length * width


def classify_triangle(a, b, c):
    if a == b:
        if a == c:
            return "equilateral"
        return "isosceles"
    elif a == c:
        return "isosceles"
    elif b == c:
        return "isosceles"
    return "various"

