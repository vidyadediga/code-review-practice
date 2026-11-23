def add(a,b):
    return a+b

print(add(10,4))

def subtract(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    return a - b