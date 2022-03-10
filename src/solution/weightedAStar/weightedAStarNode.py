from game.state.gameState import GameState
from utils.point import Point


class WeightedAStarNode:
  
  def __init__(self, _gameState: GameState, _solutionLength: int, _moves: str, alpha: float, _parent = None):
    self.gameState = _gameState
    self.solutionLength = _solutionLength
    self.moves = _moves
    
    self.parent = _parent
    
    self.estimatedCost = self.solutionLength
    self.estimatedCost += alpha * Point.manhattanDistance(self.gameState.gandalfState.position, self.gameState.board.goalPosition)