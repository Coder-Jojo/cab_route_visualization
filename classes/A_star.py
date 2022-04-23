import pygame
import numpy as np
import math
import time

class Node:
    def __init__(self, grid, loc=(0,0)):
        self.loc=loc
        self.parent=None
        self.congestion = grid.congestion[(loc[0]*grid.cols)+loc[1]]
        self.g = self.congestion
        self.h = 0
        self.path_len = 1

    # function for comparing equality between two nodes
    def __eq__(self, otherNode):
        return self.loc == otherNode.loc

    @property
    def f(self):
        return self.h + self.g


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
    x, y = currentNode.loc
    n, m = grid.rows, grid.cols
    childNodes = []
    if x-1>=0 and grid.matrix[x-1][y]>0:
        childNodes.append(Node(grid, loc=(x-1,y)))
    if y-1>=0 and grid.matrix[x][y-1]>0:
        childNodes.append(Node(grid, loc=(x,y-1)))
    if x+1<n and grid.matrix[x+1][y]>0:
        childNodes.append(Node(grid, loc=(x+1,y)))
    if y+1<m and grid.matrix[x][y+1]>0:
        childNodes.append(Node(grid, loc=(x,y+1)))

    return childNodes


def search_path(start, end, grid, name):

    # creating Open and closed Lists
    openList = []
    closedList = []
    closed_set = set()

    # inserting the first node in the open list
    openList.append(start)

    visited = []

    # traversing the graph using A* algorithm
    while len(openList):

        # find the node with minimum cost
        currentNode, index = find_min_node(openList)
        openList.pop(index)
        closedList.append(currentNode)
        closed_set.add(currentNode.loc)

        grid.a_star_cells(currentNode.loc[0], currentNode.loc[1], '#80FF00')
        grid.put_path(name, currentNode.loc[0] * grid.size, currentNode.loc[1] * grid.size)
        visited.append(currentNode.loc)

        # if the goal node is reached then break
        if currentNode == end:
            break

        # find all the children of current Node
        children = get_child_nodes(currentNode, grid)

        # add the new child to the openList
        for child in children:

            if child.loc in closed_set:                             # if child already in closed list, do nothing
                continue

            child.g = currentNode.g + 1 + child.congestion
            child.h = manhattan(child.loc, end.loc)
            child.parent = currentNode

            for open_node in openList:
                if child == open_node and child.g > open_node.g:
                    continue

            openList.append(child)
            grid.a_star_cells(child.loc[0], child.loc[1], '#FFFF00')
            visited.append(child.loc)
            time.sleep(.05)

    grid.get_back_congestion_road(visited)
    return closedList                                       # return closed list for finding the path


def path(start, closedList, grid, end):

    path = []

    if len(closedList) == 1:
        print('Could not find the path because roads are disjoint.', 'Run the algorithm again')
        grid.force_stop()
        return path

    # start with the goal node and backtrack to the starting node by visiting
    # parents of each backtracked node
    currentNode = closedList[-1]

    while currentNode != start:
        path.append(currentNode.loc)
        currentNode = currentNode.parent
    path.append(currentNode.loc)

    return path


