def add(x, y):
    return x+y
def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        raise ValueError
