def outer():
    print("outer function executed")
    def inner():
        print("inner funtion executed")
    print("inner function will executed")
    return inner
f1 = outer()
f1()

