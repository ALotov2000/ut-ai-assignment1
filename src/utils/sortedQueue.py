from heapq import heappush, heappop

class Node:
  def __init__(self, _item, _value: int) -> None:
    self.item = _item
    self.value = _value
  
  def __lt__(self, other) -> bool:
    return self.value < other.value

class SortedQueue:
  
  def __init__(self):
    self._queue = list()
    
  def enqueue(self, item, value: int):
    heappush(self._queue, Node(item, value))
       
  
  def dequeue(self):
    if len(self._queue) == 0:
      return None
    
    return heappop(self._queue).item