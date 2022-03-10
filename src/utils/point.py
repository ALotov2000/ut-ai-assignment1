class Point:
  
  def __init__(self, _x, _y) -> None:
    self.x = _x
    self.y = _y
  
  def left(self):
    return Point(self.x - 1, self.y)
  
  def right(self):
    return Point(self.x + 1, self.y)
  
  def bottom(self):
    return Point(self.x, self.y + 1)
  
  def top(self):
    return Point(self.x, self.y - 1)
  
  def __eq__(self, other) -> bool:
    return self.x == other.x and self.y == other.y
  
  def __lt__(self, other) -> bool:
    return self.x < other.x and self.y < other.y
  
  def __ge__(self, other) -> bool:
    return self.x >= other.x and self.y >= other.y
  
  def __repr__(self) -> str:
    return '(' + str(self.x) + ' ' + str(self.y) + ')'
  
  def isBetween(self, first, last) -> bool:
    return self >= first and self < last
  
  @staticmethod
  def manhattanDistance(first, second):
    return abs(first.x - second.x) + abs(first.y - second.y)