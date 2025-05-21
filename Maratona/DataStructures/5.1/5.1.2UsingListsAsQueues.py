

from collections import deque

queue = deque(["Eric", "John", "Michael"]) # Fila atual

queue.append("Terry") # Terry chega

queue.append("Graham") # Graham Chega

print(queue.popleft()) # O Eric sai

print(queue.popleft()) # O John sai

print(queue) # Michael, Terry e Graham