import threading
import time
import random

items = []

def producer(c):
    while True:    
        c.acquire()
        item = random.randint(1,100)
        print("Producer producing item:",item)
        items.append(item)
        print("Producer giving notification")
        c.notify()
        c.release()
        time.sleep(5)

def consumer(c):
    while True:
        c.acquire()
        print("Consumer waiting for updation")
        c.wait()
        print("Consumer got update consuming item:",items.pop())
        c.release()
        time.sleep(5)

c = threading.Condition()
t1  = threading.Thread(target=consumer,args=(c,))
t2 = threading.Thread(target=producer,args=(c,))
t1.start()
t2.start()

