# import threading

# current_thread  = threading.current_thread().name
# print(f"The current thread name is:{current_thread}")

# threading.current_thread().name = "Mohit wage"

# print("the new thread name is:",threading.current_thread().name)

import threading 

current_Thread = threading.current_thread().name
print(f"The current thread name is :{current_Thread}")

threading.current_thread().name= "Mohit wage"

print("The new thread name is : ",threading.current_thread().name)


