def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def division(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y