# Разработайте и протестируйте метод numberInInterval, который проверяет,
# попадает ли переданное число в интервал (25;100).

def number_in_interval(n: int) -> bool:
    return n in range(25, 101)
