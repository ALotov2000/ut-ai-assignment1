from game.creature.creature import Creature
from utils.point import Point


class Building(Creature):
  
  def __init__(self, _position: Point) -> None:
    super().__init__(_position)