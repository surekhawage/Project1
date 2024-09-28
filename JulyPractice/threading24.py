import threading
import time

I = threading.Lock()

def wish(name):
    I.acquire()
    try :
        for i in range(10):
            print("Good morning",end=' ')
            time.sleep(1)
            print(name)
    finally:
        I.release()

t1 = threading.Thread(target=wish,args=("Mohit",))
t2 = threading.Thread(target=wish,args=("Rohit",))
t3 = threading.Thread(target=wish,args=("Amit",))
t1.start()
t2.start()
t3.start()
