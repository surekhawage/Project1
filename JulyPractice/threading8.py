import threading
import time

def display():
    print(threading.current_thread().name,"..started..")
    time.sleep(3)
    print(threading.current_thread().name,"..ended..")
    
print("the Number of threads:",threading.active_count())
t1 = threading.Thread(target=display,name="ChildThread1")
t2 = threading.Thread(target=display,name="ChildThread2")
t3 = threading.Thread(target=display,name="ChildThread3")
t1.start()
t2.start()
t3.start()

I = threading.enumerate()

for t in I:
    print("Thread name:",t.name)

time.sleep(5)

I = threading.enumerate()

for t in I:
    print("Thread name:", t.name)



# import threading
# import time
# def display():
#     print(threading.current_thread().name,"..started..")
#     time.sleep(3)
#     print(threading.current_thread().name,"..end..")

# print("The Number of threads:",threading.active_count())
# t1 = threading.Thread(target=display,name="childThread1")
# t2 = threading.Thread(target=display,name="childThread2")
# t3 = threading.Thread(target=display,name="childThread3")

# t1.start()
# t2.start()
# t3.start()

# I = threading.enumerate()

# for t in I :
#     print("Thread :", t.name)
# time.sleep(5)

# I = threading.enumerate()
# for t in I :
#     print("Thread :", t.name)
