from collections import deque

myQueue= deque()

myQueue.append(1)
myQueue.append(2)
myQueue.append(3)
myQueue.appendleft(100)

for value in myQueue:
      print(value,end="  ")