
from typing import List
from game.creature.fellow import Fellow
from game.board import Board
from game.creature.building import Building
from game.creature.orc import Orc
from game.state.code.fellowStateCode import FellowStateCode
from game.state.enemyState import EnemyState
from game.state.gameState import GameState
from game.state.gandalfState import GandalfState
from utils.point import Point


def formulateTestCase(addr: str):
  
  with open(addr) as inputFile:
    n, m = map(int, inputFile.readline().split())
    sy, sx = map(int, inputFile.readline().split())
    dy, dx = map(int, inputFile.readline().split())
    k, l = map(int, inputFile.readline().split())
    e = list()
    for i in range(k):
      e.append(tuple(map(int, inputFile.readline().split())))
    
    f = list()
    for i in range(l):
      f.append(tuple(map(int, inputFile.readline().split())))
      
    b = list()
    for i in range(l):
      b.append(tuple(map(int, inputFile.readline().split())))
      
  # print((m, n), (sx, sy), (dx, dy), e, f, b, sep='\n')
  
  rowCount = n
  colCount = m
  fellowCount = l
  enemyCount = k
  goal = Point(dx, dy)
  
  fellowList = list()
  for i in range(fellowCount):
    newBuilding = Building(Point(b[i][1], b[i][0]))
    newFellow = Fellow(Point(f[i][1], f[i][0]), newBuilding)
    fellowList.append(newFellow)
    
  enemyList = list()
  for i in range(enemyCount):
    newOrc = Orc(Point(e[i][1], e[i][0]), e[i][2])
    enemyList.append(newOrc)
  
  board = Board(rowCount, colCount, fellowCount, enemyCount, fellowList, enemyList, goal)
  
  
  gandalfState = GandalfState(Point(sx, sy), None)
  fellowshipState = [FellowStateCode.InInitPlace for i in range(fellowCount)]
  enemyState = EnemyState(None)
  initState = GameState(board, gandalfState, fellowshipState, enemyState, 0)
  
  return board, initState
    
    
  