import threading
import time

def producer():
    time.sleep(4)
    print("Producer thread producing threads")
    time.sleep(3)
    print("producer thread giving notification by setting event")
    event.set()

def consumer():
    print("Consumer thread is waiting for production")
    event.wait()
    time.sleep(3)
    print("Consumer thread got notification and consuming items")

event = threading.Event()
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start()
t2.start()


