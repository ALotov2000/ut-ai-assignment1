from game.creature.creature import Creature
from utils.point import Point


class Orc(Creature):
  
  def __init__(self, _position: Point, _degree: int) -> None:
    super().__init__(_position)
    self.degree = _degree