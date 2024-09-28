import threading
import time

def double(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double:",2*n)

def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print("Squares:",n*n)

numbers= [1,2,3,4,5,6]
begintime = time.time()
t1 = threading.Thread(target=double,args=(numbers,))
t2= threading.Thread(target=squares,args=(numbers,))

t1.start()
t2.start()
t1.join()
t2.join()

print("The Total time taken:",time.time()-begintime)    
