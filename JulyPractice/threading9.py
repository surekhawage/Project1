import threading
import time

def display():
    print(threading.current_thread().name,"..started..")
    time.sleep(3)
    print(threading.current_thread().name,"..end..")

print("The number of threads :", threading.active_count())

t1 = threading.Thread(target=display,name="ChildThread1")
t2 = threading.Thread(target=display,name="ChildThread2")
t1.start()
t2.start()

print(t1.name,"is alive",t1.is_alive())
print(t2.name,"is alive",t2.is_alive())
time.sleep(5)
print(t1.name,"is alive",t1.is_alive())
print(t2.name,"is alive",t2.is_alive())

