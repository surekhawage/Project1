import threading
import time

I = threading.Lock()

def wish(name):
    with I:
        for i in range(10):
            print("Good morning",end="")
            time.sleep(2)
            print(name)
        
t1 = threading.Thread(target=wish,args=("Mohit",))
t2 = threading.Thread(target=wish,args=("wage",))
t3 = threading.Thread(target=wish,args=("Guy",))
t1.start()
t2.start()
t3.start()
