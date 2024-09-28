import threading

def test():
    print("Child thread")

t = threading.Thread(target=test)
t.start()
print("The main thread ID:",threading.current_thread().ident)
