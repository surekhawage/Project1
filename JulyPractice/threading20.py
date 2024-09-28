import threading
import time

def consumer(c):
    c.acquire()
    print("Consumer waiting for updation")
    c.wait()
    print("Consumer got notification, consuming item")
    c.release()
def producer(c):
    c.acquire()
    print("Producer producing items")
    print("Producer notifying consumer")
    c.notify()
    c.release()

c  = threading.Condition()
t1 = threading.Thread(target=consumer,args=(c,))
t2 = threading.Thread(target=producer,args=(c,))
t1.start()
t2.start()
