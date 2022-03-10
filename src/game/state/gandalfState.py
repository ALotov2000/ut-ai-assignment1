from game.creature.fellow import Fellow
from utils.point import Point


class GandalfState:
  
  def __init__(self, _position: Point, _carriedFellowIndex: int | None) -> None:
    self.position = _position
    self.carriedFellowIndex = _carriedFellowIndex