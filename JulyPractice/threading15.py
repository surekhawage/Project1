import threading

I = threading.RLock()

def factorial(n):
    I.acquire()
    if n==0:
        result = 1
    else:
        result = n*factorial(n-1)
    I.release()
    return result

def results(n):
    print("The factorial of",n,"is",factorial(n))

t1 = threading.Thread(target=factorial,args=(5,))
t2 = threading.Thread(target=factorial,args=(11,))
t1.start()
t2.start()

