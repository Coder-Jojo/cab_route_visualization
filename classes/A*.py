import pygame
import numpy as np
import math   

class Node:
   def __init__(self, grid, loc=(0,0)):
      self.loc=loc
      self.parent=None
      self.f=self.g= grid.congestion[(loc[0]*grid.cols)+loc[1]] + grid.matrix[loc[0]][loc[1]]
      self.h=0  

'''def g_value(grid):
   return grid.congestion((node.loc[0]*grid.cols)+node.loc[1]) + grid.matrix[node.loc[0]][node.loc[1]]''' 
   
def manhattan(x,y):
  return abs(x[0]-y[0]) + abs(x[1]-y[1])
  
def find_min_node(openList):
   currentIndex=0
   currentNode=openList[0]
   
   for index,node in enumerate(openList):
      if node.f<currentNode.f:
         currentIndex=index
         currentNode=node
         
   return currentNode, currentIndex
   
def get_child_nodes(currentNode, grid):
   x,y = currentNode.loc
   childNodes=[]
   if grid.matrix[x-1][y]>0 and x-1>=0:
      childNodes.append(Node(grid, loc=(x-1,y)))
   if grid.matrix[x][y-1]>0 and y-1>=0:
      childNodes.append(Node(grid, loc=(x,y-1)))
   if grid.matrix[x+1][y]>0 and x+1<100:
      childNodes.append(Node(grid, loc=(x+1,y)))
   if grid.matrix[x][y+1]>0 and y+1<100:
      childNodes.append(Node(grid, loc=(x,y+1)))
   
   return childNodes
   
def search_path(start, end, grid):

  # creating Open and closed Lists
  openList = []
  closedList = []

  # inserting the first node in the open list
  openList.append(start)

  # traversing the graph using A* algorithm
  while len(openList):

    # find the node with minimum cost
    currentNode, index = find_min_node(openList)
    openList.pop(index)

    # add currentNode in closed list
    closedList.append(currentNode)

    # if the goal node is reached then break
    if currentNode == end:
      break
    
    # find all the children of current Node
    children = get_child_nodes(currentNode, grid)

    # add the new child to the openList
    for child in children:

      if child in closedList:                             # if child already in closed list, do nothing
        continue

      if child in openList:                               # if child in openList then update cost
        child.g = min(child.g, currentNode.g + 1)
        child.h = manhattan(child.loc, end.loc)
        child.f = child.g + child.h
        child.parent = currentNode
        continue
      
      child.h = manhattan(child.loc, end.loc)    # calculating f = g + h
      child.f = child.g + child.h

      child.parent = currentNode                          # adding parent to the child

      openList.append(child)

  return closedList                                       # return closed list for finding the path
  
def path(start, closedList, grid, end):

  path = []
  print(closedList)

  # start with the goal node and backtrack to the starting node by visiting
  # parents of each backtracked node
  currentNode = closedList[-1]
  
  while currentNode != start:
    path.append(currentNode.loc)
    currentNode = currentNode.parent
  path.append(currentNode.loc)
  
  return path


