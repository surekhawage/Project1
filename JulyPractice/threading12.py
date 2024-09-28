import threading
import time

def display():
    for i in range(10):
        print("lazy thread")
        time.sleep(2)

t = threading.Thread(target=display)
t.setDaemon(True)
t.start()
time.sleep(2)
print("End of main thread")

