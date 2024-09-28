import threading 
import time

I = threading.RLock()

I.acquire()
print("Hey acquired")
I.acquire()
print("hey acquired again")

