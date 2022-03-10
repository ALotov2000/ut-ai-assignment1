from game.board import Board
from game.state.gameState import GameState
from solution.ids.idsNode import IdsNode
from solution.utils.getNext import getNext
from utils.point import Point
from utils.stack import Stack

class Ids:
  visitedStateCount: int = None
  
  @staticmethod
  def solve(board: Board, initGameState: GameState):
    Ids.visitedStateCount = 0

    maxDepth = Point.manhattanDistance(initGameState.gandalfState.position, board.goalPosition) % 2
    maxDepth = 2 - maxDepth
    while True:
      # print(maxDepth)
      dfsResult = Ids.solveDfs(board, initGameState, maxDepth)
      
      if dfsResult is not None:
        return dfsResult
      
      maxDepth += 2
    
  @staticmethod 
  def solveDfs(board: Board, initGameState: GameState, maxDepth: int):
    
    initNode = IdsNode(initGameState, 0, '', None)
    frontier = Stack()
    frontier.push(initNode)
    
    visited = [[[list() for k in range(board.fellowCount + 1)] for j in range(board.rowCount)] for i in range(board.colCount)]
    visited[initNode.gameState.gandalfState.position.x][initNode.gameState.gandalfState.position.y][initNode.gameState.inGoalCount].append(initNode)
    
    while True:
      node: IdsNode = frontier.pop()
      
      if node is None:
        return None
      
      # print(node.gameState.gandalfState.position, node.gameState.fellowshipState)
         
      if node.gameState.isGoal():
        return node
      
      if node.solutionLength >= maxDepth:
        continue
      
      
      nextStates = getNext(node.gameState)
      Ids.visitedStateCount += len(nextStates)
      
      for (gameState, nextMove) in nextStates:
        # print('\t', gameState.gandalfState.position, gameState.fellowshipState)
        
        newNode = IdsNode(gameState, node.solutionLength + 1, node.moves + nextMove, node)
        
        isVisited = False
        for visitedNode in visited[newNode.gameState.gandalfState.position.x][newNode.gameState.gandalfState.position.y][newNode.gameState.inGoalCount]:
          if visitedNode.gameState == gameState and visitedNode.solutionLength <= newNode.solutionLength:
            isVisited = True
            break
        
        if isVisited:
          continue
        
        visited[newNode.gameState.gandalfState.position.x][newNode.gameState.gandalfState.position.y][newNode.gameState.inGoalCount].append(newNode)
        frontier.push(newNode)