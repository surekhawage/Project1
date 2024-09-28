import threading 
import time

def trafficPolice():
    while True:
        time.sleep(10)
        print("Traffic Police Giving GREEN Signal ")
        event.set()
        time.sleep(20)
        print("Traffic police Giving RED Signal")
        event.clear()
def driver():
    num = 0
    while True:
        print("Drivers waiting for GREEN Signal")
        event.wait()
        print("Traffic Signal is GREEN... vehicles can move")
        while event.isSet():
            num = num+1
            print("Vehicle No:",num,"Crossing the signal")
            time.sleep(2)
        print("Traffic Signal is RED... Drivers have to wait")

event = threading.Event()
t1 = threading.Thread(target=trafficPolice)
t2 = threading.Thread(target=driver)
t1.start()
t2.start()

