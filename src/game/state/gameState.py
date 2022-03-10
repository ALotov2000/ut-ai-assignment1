from audioop import getsample
from typing import List
from game.board import Board
from game.exception.orcAwakenException import OrcAwakenException
from game.exception.outOfBoxException import OutOfBoxException
from game.state.code.fellowStateCode import FellowStateCode

from game.state.gandalfState import GandalfState
from game.state.enemyState import EnemyState
from utils.point import Point


class GameState:
  
  def __init__(self, _board: Board, _gandalfState: GandalfState, _fellowshipState: List[int], _enemyState: EnemyState, _inGoalCount: int = 0) -> None:
    self.board = _board
    
    self.gandalfState = _gandalfState
    self.fellowshipState = _fellowshipState
    self.enemyState = _enemyState
    
    self.inGoalCount = _inGoalCount
    
    self.hash = self.__hash__()
  
  
  def __hash__(self):
    h = 0
    h += self.gandalfState.position.x * 100 + self.gandalfState.position.y
    if self.enemyState.orcIndex is not None:
      h += (self.enemyState.orcIndex * 10 + self.enemyState.distractionLevel) * 10000
    for i in range(self.board.fellowCount):
      h += self.fellowshipState[i] * (10 ** i) * 10000000
    return h
  
  def isGoal(self):
    return self.gandalfState.position == self.board.goalPosition and self.inGoalCount == self.board.fellowCount
      
  def __eq__(self, other):
    return self.hash == other.hash
    # if self.gandalfState.position != other.gandalfState.position:
    #   return False
    
    # if self.enemyState.orcIndex != other.enemyState.orcIndex:
    #   return False
    # if self.enemyState.orcIndex is not None and self.enemyState.distractionLevel != other.enemyState.distractionLevel:
    #   return False
    
    # if self.inGoalCount != other.inGoalCount:
    #   return False
    # for i in range(self.board.fellowCount):
    #   if self.fellowshipState[i] != other.fellowshipState[i]:
    #     return False
    
    # return True
  
  def getLeft(self):
    newGandalfState = GandalfState(self.gandalfState.position.left(), self.gandalfState.carriedFellowIndex)
    return self.applyGandalfStateChange(newGandalfState)
    
  def getRight(self):
    newGandalfState = GandalfState(self.gandalfState.position.right(), self.gandalfState.carriedFellowIndex)
    return self.applyGandalfStateChange(newGandalfState)
    
  def getTop(self):
    newGandalfState = GandalfState(self.gandalfState.position.top(), self.gandalfState.carriedFellowIndex)
    return self.applyGandalfStateChange(newGandalfState)
    
  def getBottom(self):
    newGandalfState = GandalfState(self.gandalfState.position.bottom(), self.gandalfState.carriedFellowIndex)
    return self.applyGandalfStateChange(newGandalfState)
    
  def applyGandalfStateChange(self, newGandalfState: GandalfState):
    
    if not newGandalfState.position.isBetween(Point(0, 0), Point(self.board.colCount, self.board.rowCount)):
      raise OutOfBoxException()
    
    newState = GameState(self.board, newGandalfState, self.fellowshipState.copy(), self.enemyState, self.inGoalCount)
    newState.applyChanges()     
    return newState
    
    
    
    
  def applyChanges(self):
    
    self.applyChangesEnemy()
    self.applyChangesGoalAchieved()
    self.applyChangesNewFriend()
      
  
  
  
    
  def applyChangesEnemy(self):
    
    x = self.gandalfState.position.x
    y = self.gandalfState.position.y
    
    if self.board.orcTable[x][y] is not None:
      raise OrcAwakenException()
    
    i = self.board.coverTable[x][y]
    
    if self.enemyState.orcIndex is not None and i == self.enemyState.orcIndex:
      self.enemyState = EnemyState(self.enemyState.orcIndex, self.enemyState.distractionLevel + 1)
    else: 
      self.enemyState = EnemyState(i, 1)
    
    if self.enemyState.orcIndex is not None and self.enemyState.distractionLevel > self.board.enemyList[self.enemyState.orcIndex].degree:
      raise OrcAwakenException()
  
  def applyChangesGoalAchieved(self):
    
    x = self.gandalfState.position.x
    y = self.gandalfState.position.y
    
    if self.gandalfState.carriedFellowIndex is not None:
      i = self.board.buildingTable[x][y]
      if i is not None and self.gandalfState.carriedFellowIndex == i:
        self.fellowshipState[i] = FellowStateCode.InGoalPlace
        self.inGoalCount += 1
        self.gandalfState = GandalfState(self.gandalfState.position, None)
            
  def applyChangesNewFriend(self):
    
    x = self.gandalfState.position.x
    y = self.gandalfState.position.y
    
    
    if self.gandalfState.carriedFellowIndex is None:  
      i = self.board.fellowTable[x][y]
      if i is not None and self.fellowshipState[i] == FellowStateCode.InInitPlace:
        self.gandalfState = GandalfState(self.gandalfState.position, i)
        self.fellowshipState[i] = FellowStateCode.WithGandalf
