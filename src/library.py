from queue import PriorityQueue
from copy import deepcopy
import random
import time
from node import node
import os
from pathlib import Path

# Output
def printNode(node):
    # For debugging and output purpose
    print(node.noNode)
    printMatrix(node.matrix)
    print()

def printMatrix(matrix):
    # For debugging purpose
    for i in range(4):
        for j in range(4):
            print("%3d"%matrix[i][j], end = " ")
        print()

def printTableKurang(tableKurang):
    # Prints the values of Kurang(i) of all numbers in puzzle, 1-16
    # 16 marks the empty tile
    tableKurang.sort(reverse=False)
    print("Value of each element's Kurang(i):")
    for i in range(len(tableKurang)):
        print("[ " + str("%2d"%tableKurang[i][0]) + " | " + str("%2d"%tableKurang[i][1]) + " ]")

def printPath(node, numStep):
    dictDir = {
        0: "UP",
        1: "RIGHT",
        2: "DOWN",
        3: "LEFT"
    }
    # print the path from the root node to the goal node
    if (node.parent.parent != None):
        printPath(node.parent, numStep+1)
    else:
        print("Depth : " + str(numStep+1))
    print(dictDir[node.movement], end=" ")
    printNode(node)

def welcome():
    print(" 11  5555     PPPP               l          SSS      l             ")
    print("111  5        P   P              l         S         l             ")
    print(" 11  555  --- PPPP  u  u zz  zz  l eee      SSS  ooo l v v eee rrr ")
    print(" 11     5     P     u  u  z   z  l e e         S o o l v v e e r   ")
    print("11l1 555      P      uuu  zz  zz l ee      SSSS  ooo l  v  ee  r   ")
    print()

# Conversion
def toArray(matrix):
    # convert matrix to array
    arr = []
    for i in range(4):
        for j in range(4):
            arr.append(matrix[i][j])
    return arr

# Initialize Puzzle
def initiate():
    # Input puzzle, either from random function or file provided
    choice = int(input("Make a choice!\n1. Input from randomizer\n2. Input from file\nYour choice: "))
    tempMat = []

    if (choice == 1):
        randomData = random.sample(range(1, 17), 16)
        tempMat = [[0 for j in range(4)] for i in range(4)]
        for i in range(4):
            for j in range(4):
                tempMat[i][j] = randomData[i*4 + j]
        printMatrix(tempMat)
    else:
        # Ask for file name input (including extension)
        fileName = input("Enter file name: ")

        # Read from File and Store to Matrix
        currPath = os.path.dirname(__file__)
        relPath = os.path.relpath("Tucil3_13520019\\test\\" + fileName, currPath)
        file = open(Path(relPath), "r")
        lines = file.readlines()
        
        for line in lines:
            # split to list of integers
            tempMat.append(list(map(lambda x : int(x), line.split())))
    
    return tempMat

# Initialize Node
def deriveNode(oldMat, oldEmptyTile, movement, level, parent, noNewNode):
    # make a new node with empty tile moved to either up right down or left
    newMat = deepcopy(oldMat)
    # List of additions to directions empty tile movement: up right down left (0,1,2,3)
    add_row = [-1, 0, 1, 0]
    add_col = [0, 1, 0, -1]
    
    oldX = oldEmptyTile[0]
    oldY = oldEmptyTile[1]
    
    newX = oldEmptyTile[0] + add_row[movement]
    newY = oldEmptyTile[1] + add_col[movement]

    if (checkIndex((newX, newY))):
        newMat[oldX][oldY], newMat[newX][newY] = newMat[newX][newY], newMat[oldX][oldY]
        newNode = node(parent, newMat, (newX, newY), noNewNode, movement, level, calcCi(level, newMat))
        return newNode
    else:
        return None

# Functions
def findEmptyNode(matrix):
    # find the empty tile position
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] == 16):
                return i, j

# Cost estimation
def calcGi(matrix):
    # calculate misplaced tiles
    misplaced = 0
    ctr = 1
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] != ctr):
                misplaced += 1
            ctr += 1
    return misplaced

def calcCi(depth, matrix):
    # calculate cost, with formula c(i) = f(i) + g(i)
    # c(i) = cost
    # f(i) = depth (or level)
    # g(i) = number of misplaced tiles
    return depth + calcGi(matrix)

# Checks
def checkSolvable(mat):
    # check value of Sigma Kurang(i) + X which determines
    # if the puzzle is solvable or not
    tableKurang = []
    totalKurang = 0
    temp = toArray(mat)
    for i in range(0,16):
        kurang = 0
        for j in range(i+1,16):
            if(temp[i]>temp[j]):
                kurang+=1
        tableKurang.append([temp[i], kurang])
        totalKurang += kurang
    i, j = findEmptyNode(mat)
    x = (i + j) % 2
    return ((totalKurang+x) % 2 == 0), tableKurang, totalKurang + x, i, j

def checkPresent(dict, matrix, cost):
    # return true if present in dict and need not to be updated
    if (str(toArray(matrix)) in dict):
        if (dict[str(toArray(matrix))] < cost):
            return True
    return False

def checkIndex(emptyTile):
    # check if movement of empty tile is valid (between 0 and 3 (inclusive)) or not
    return (emptyTile[0] >= 0 and emptyTile[0] < 4 and emptyTile[1] >= 0 and emptyTile[1] < 4)

def noContradictMovement(last, now):
    # return true if not contradicting (the last move was up, on this move, can't go down)
    return ((last == 4) or (last == 0 and now != 2) or (last == 2 and now != 0) or (last == 1 and now != 3) or (last == 3 and now != 1))

# Main Function using Branch and Bound Algorithm
def solve(tempMatrix, dict, tempEmptyTile):
    # Solve the N Puzzle using Branch and Bound Algorithm
    start = time.time()

    # make the root node
    rootNode = node(None, tempMatrix, tempEmptyTile, 1, 4, 0, calcCi(0, tempMatrix))

    # put the root to Priority Queue, sorted from min to max.
    pq = PriorityQueue()
    pq.put((rootNode.ci, rootNode))

    # number of steps taken to reach solution node
    numStep = 0

    # number of node
    ctrNoNode = 1
    while not pq.empty():
        # get first element in Priority Queue (the one with the least cost)
        ci, eNode = pq.get()

        # if reaching the goal state
        if (calcGi(eNode.matrix) == 0):
            end = time.time()
            printPath(eNode, numStep)
            print()
            print("Execution time: " + str(end-start))
            print()
            print("Number of nodes generated: " + str(ctrNoNode))
            break
        
        # try moves to four directions, if possible
        for i in range(4):
            if (noContradictMovement(eNode.movement, i)):
                childNode = deriveNode(eNode.matrix, eNode.emptyTile, i, eNode.fi + 1, eNode, ctrNoNode + 1)

                if (childNode != None and not checkPresent(dict, childNode.matrix, childNode.ci)):
                    # put new node to Priority Queue and Dictionary
                    pq.put((childNode.ci, childNode))
                    dict[str(toArray(childNode.matrix))] = childNode.ci
                    ctrNoNode += 1