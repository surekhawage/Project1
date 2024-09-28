import threading
import time

def display():
    print(threading.current_thread().name,"..started..")
    time.sleep(3)
    print(threading.current_thread().name,"..ended..")

print("The number of threads",threading.active_count())
t1 = threading.Thread(target=display,name = "childThread1")
t2 = threading.Thread(target=display,name = "childThread2")
t3 = threading.Thread(target=display,name = "childThread3")
t1.start()
t2.start()
t3.start()
print("The NUmber of threads:",threading.active_count())
time.sleep(5)
print("The Number of threads:",threading.active_count())
