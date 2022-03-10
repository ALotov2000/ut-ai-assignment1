from typing import List
from game.creature.fellow import Fellow
from game.creature.orc import Orc
from utils.point import Point


class Board:
  
  def __init__(self, _rowCount: int, _colCount: int, _fellowCount: int, _enemyCount: int, _fellowship: List[Fellow], _enemyList: List[Orc], _goalPosition: Point) -> None:
    self.rowCount = _rowCount
    self.colCount = _colCount
    self.fellowCount = _fellowCount
    self.enemyCount = _enemyCount
    
    self.fellowship = _fellowship
    self.buildingList = [f.destination for f in _fellowship]
    self.enemyList = _enemyList
    
    self.goalPosition = _goalPosition
    
    self.initTables()
    
  def initTables(self):
    self.fellowTable = [[None for j in range(self.rowCount)] for i in range(self.colCount)]
    self.orcTable = [[None for j in range(self.rowCount)] for i in range(self.colCount)]
    self.buildingTable = [[None for j in range(self.rowCount)] for i in range(self.colCount)]
    self.coverTable = [[None for j in range(self.rowCount)] for i in range(self.colCount)]
    
    for i in range(len(self.fellowship)):
      fellow = self.fellowship[i]
      building = fellow.destination
      self.fellowTable[fellow.position.x][fellow.position.y] = i
      self.buildingTable[building.position.x][building.position.y] = i
      
    for i in range(len(self.enemyList)):
      orc = self.enemyList[i]
      self.orcTable[orc.position.x][orc.position.y] = i
      
      for x in range(max(0, orc.position.x - orc.degree), min(orc.position.x + orc.degree + 1, self.colCount)):
        remainingDegree = orc.degree - abs(orc.position.x - x)
        for y in range(max(0, orc.position.y - remainingDegree), min(orc.position.y + remainingDegree + 1, self.rowCount)):
          self.coverTable[x][y] = i
          
  def printFellowshipTable(self):
    print('fellowship table:')
    for x in range(self.colCount):
      for y in range(self.rowCount):
        i = self.fellowTable[x][y]
        if i is not None:
          print(i, end='\t')
        else:
          print('-', end='\t')
          
      print()
      
    print('* ' * 30)
    
  def printBuildingTable(self):
    print('building table:')
    for x in range(self.colCount):
      for y in range(self.rowCount):
        i = self.buildingTable[x][y]
        if i is not None:
          print(i, end='\t')
        else:
          print('-', end='\t')
          
      print()
      
    print('* ' * 30)
    
  def printOrcTable(self):
    print('orc table:')
    for x in range(self.colCount):
      for y in range(self.rowCount):
        i = self.orcTable[x][y]
        if i is not None:
          print(i, end='\t')
        else:
          print('-', end='\t')
          
      print()
      
    print('* ' * 30)
    
  def printCoverTable(self):
    print('cover table:')
    for x in range(self.colCount):
      for y in range(self.rowCount):
        i = self.coverTable[x][y]
        if i is not None:
          print(i, end='\t')
        else:
          print('-', end='\t')
          
      print()
      
    print('* ' * 30)
    
  
  def printAll(self):
    self.printFellowshipTable()
    self.printBuildingTable()
    self.printOrcTable()
    self.printCoverTable()