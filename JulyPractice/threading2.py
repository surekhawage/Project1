import threading

class My_thread(threading.Thread):
    def run(self):
        for i in range(1,11):
            print("Child Thread - 1")

t = My_thread()

t.start()

for i in range(10):
    print("Main thread-1")

