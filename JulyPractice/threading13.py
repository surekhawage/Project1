import threading
import time


I = threading.Lock()

def wish(name):
    I.acquire()
    for i in range(10):
        print("Good Evening",end="")
        time.sleep(2)
        print(name)
    I.release()

t1 = threading.Thread(target=wish,args=("Mohit",))
t2= threading.Thread(target=wish,args=("wage",))
t3= threading.Thread(target=wish,args=("Mohit wage",))
t1.start()
t2.start()
t3.start()

