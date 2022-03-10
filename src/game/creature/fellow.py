from game.creature.building import Building
from game.creature.creature import Creature
from utils.point import Point


class Fellow(Creature):
  
  def __init__(self, _position: Point, _destination: Building) -> None:
    super().__init__(_position)
    self.destination = _destination