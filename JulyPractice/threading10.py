import threading
import time

def display():
    for i in range(10):
        print("seetha")
        time.sleep(2)
    
t = threading.Thread(target=display)
t.start()

t.join(5)
for j in range(10):
    print("rama")

