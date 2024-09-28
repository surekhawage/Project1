import threading
import time

s = threading.Semaphore()

def wish(name):
    s.acquire()
    for i in range(10):
        print("Good Morning",end="")
        time.sleep(2)
        print(name)
    s.release()

t1 = threading.Thread(target=wish,args=("Mohit",))
t2 = threading.Thread(target=wish,args=("wage",))
t3 = threading.Thread(target=wish,args=("wage",))
t4 = threading.Thread(target=wish,args=("Mohit",))
t5 = threading.Thread(target=wish,args=("Mohit wage",))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
