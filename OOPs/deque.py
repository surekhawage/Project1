from collections import deque

dque=deque([10,20,30])
print(dque)

dque.append(40)
dque.append(50)
print(dque)

dque.appendleft(70)
print(dque)

dque.pop()
print(dque)

dque.popleft()
print(dque)
