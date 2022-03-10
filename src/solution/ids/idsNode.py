from game.state.gameState import GameState


class IdsNode:
  
  def __init__(self, _gameState: GameState, _solutionLength: int, _moves: str, _parent = None):
    self.gameState = _gameState
    self.solutionLength = _solutionLength
    self.moves = _moves
    
    self.parent = _parent