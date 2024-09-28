def decorator(func):
    def wrapper():
        print("Operation initiated")
        result = func()
        print("Operation completed")
        return result
    return wrapper

@decorator  
def add():
    a = 2
    b = 3
    c = a + b
    print(c)
    return c

result = add()