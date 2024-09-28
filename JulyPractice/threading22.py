import threading
import time
import queue
import random

def producer(q):
    while True:
        item = random.randint(1,100)
        print("Producer producing items:",item)
        q.put(item)
        print("Producer giving notification")
        time.sleep(5)
def consumer(q):
    while True:
        print("Consumer waiting for updation")
        print("Consumer consuming items:",q.get())
        time.sleep(5)

q = queue.Queue()
t1 = threading.Thread(target=consumer,args=(q,))
t2 = threading.Thread(target=producer,args=(q,))
t1.start()
t2.start()
