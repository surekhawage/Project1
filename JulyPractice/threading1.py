import threading 

def display():
    for i in range(1,11):
        print("Child thread")

t = threading.Thread(target=display)

t.start()

for i in range(1,11):
    print("Main thread")

