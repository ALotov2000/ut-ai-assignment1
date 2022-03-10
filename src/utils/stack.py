class Stack:
  
  def __init__(self):
    self._stack = list()
    
  def push(self, item): 
    self._stack.append(item)
  
  def pop(self):
    if len(self._stack) == 0:
      return None
    return self._stack.pop(-1)