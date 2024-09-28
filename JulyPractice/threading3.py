import threading

class Tre:
    def display(self):
        for i in range(1,11):
            print("Child thread")

obj = Tre()

t = threading.Thread(target=obj.display)
t.start()
for i in range(10):
    print("Main Thread")
