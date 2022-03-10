from game.exception.orcAwakenException import OrcAwakenException
from game.exception.outOfBoxException import OutOfBoxException
from game.state.gameState import GameState


def getNext(gameState: GameState):
    ret = list()
    try:
      ret.append((gameState.getRight(), 'R'))
    except OrcAwakenException:
      pass
    except OutOfBoxException:
      pass
    
    try:
      ret.append((gameState.getBottom(), 'D'))
    except OrcAwakenException:
      pass
    except OutOfBoxException:
      pass
      
    try:
      ret.append((gameState.getTop(), 'U'))
    except OrcAwakenException:
      pass
    except OutOfBoxException:
      pass
      
    try:
      ret.append((gameState.getLeft(), 'L'))
    except OrcAwakenException:
      pass
    except OutOfBoxException:
      pass
      
          
    return ret