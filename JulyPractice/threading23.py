import threading
import queue

#other than numeric

q = queue.PriorityQueue()
q.put((3,"Mohit"))
q.put((4,"Wage"))
q.put((1,"Hey"))
q.put((2,"Mrs."))

while not q.empty():
    print(q.get()[1],end=" ")

#Priority Queue
#it gives in ascending in ascending
# q = queue.PriorityQueue()
# q.put(10)
# q.put(5)
# q.put(20)
# q.put(15)
# while not q.empty():
#     print(q.get(),end=" ")

#LIFO Queue

# q = queue.LifoQueue()
# q.put(10)
# q.put(5)
# q.put(20)
# q.put(15)
# while not q.empty():
#     print(q.get(),end=" ")

#FIFO Queue
# q = queue.Queue()
# q.put(10)
# q.put(5)
# q.put(20)
# q.put(15)

# while not q.empty():
#     print(q.get(),end=" ")

