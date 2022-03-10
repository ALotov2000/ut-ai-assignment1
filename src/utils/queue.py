class Queue:
  
  def __init__(self):
    self._queue = list()
    
  def enqueue(self, item): 
    self._queue.append(item)
  
  def dequeue(self):
    if len(self._queue) == 0:
      return None
    return self._queue.pop(0)