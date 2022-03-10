from game.board import Board
from game.state.gameState import GameState
from solution.bfs.bfsNode import BfsNode
from solution.utils.getNext import getNext
from utils.queue import Queue


class Bfs:
  visitedStateCount: int = None
  
  @staticmethod
  def solve(board: Board, initGameState: GameState):
    Bfs.visitedStateCount = 1
  
    frontier = Queue()
    
    initNode = BfsNode(initGameState, 0, '', None)
    frontier.enqueue(initNode)
    
    visited = [[[list() for k in range(board.fellowCount + 1)] for j in range(board.rowCount)] for i in range(board.colCount)]
    visited[initNode.gameState.gandalfState.position.x][initNode.gameState.gandalfState.position.y][initNode.gameState.inGoalCount].append(initNode)
      
    while True:
      
      node: BfsNode = frontier.dequeue()
      
      if node is None:
        return None
      
      # print(node.gameState.gandalfState.position, node.gameState.fellowshipState)
      
      if node.gameState.isGoal():
        return node
      
      
      nextStates = getNext(node.gameState)
      Bfs.visitedStateCount += len(nextStates)
      for (gameState, nextMove) in nextStates:
        
        # print('\t', gameState.gandalfState.position, gameState.fellowshipState)
        
        newNode = BfsNode(gameState, node.solutionLength + 1, node.moves + nextMove, node)
        
        isVisited = False
        for visitedNode in visited[newNode.gameState.gandalfState.position.x][newNode.gameState.gandalfState.position.y][newNode.gameState.inGoalCount]:
          if visitedNode.gameState == gameState:
            isVisited = True
            break
        
        if isVisited:
          continue
        
        visited[newNode.gameState.gandalfState.position.x][newNode.gameState.gandalfState.position.y][newNode.gameState.inGoalCount].append(newNode)
        frontier.enqueue(newNode)