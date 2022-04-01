from PriorityQueue import PriorityQueue
from Node import Node
import time
import random

dict = {
    0: "UP",
    1: "RIGHT",
    2: "DOWN",
    3: "LEFT"
}

def printPath(node):
    # print the path from the root node to the goal node
    if (node.parentNode.parentNode != None):
        printPath(node.parentNode)
    print(dict[node.movement], end=" ")

def printTableKurang(tableKurang):
    for i in range(len(tableKurang)):
        print("[ " + str("%2d"%tableKurang[i][0]) + " | " + str("%2d"%tableKurang[i][1]) + " ]")

def printNode(node):
    print(node.noNode)
    printMatrix(node.matrix)
    print(node.ci)
    print("\n")

def printMatrix(matrix):
    for i in range(4):
        for j in range(4):
            print(matrix[i][j], end=" ")
        print()

def isGoal(matrix):
    # check if the puzzle is solved
    ans = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,-1]]
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] != ans[i][j]):
                return False
    return True

def calcGi(matrix):
    # calculate misplaced tiles
    misplaced = 0
    ans = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,-1]]
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] != ans[i][j]):
                misplaced += 1
    return misplaced
    
def calcCi(fi, matrix):
    # calculate the cost of the node
    return fi + calcGi(matrix)

def copyMat(matrix):
    tempNewMat = [[0 for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            tempNewMat[i][j] = matrix[i][j]
    return tempNewMat

def deriveNode(oldNode, oldEmptyTile, newEmptyTile, noNode, movement):
    # copy to make a new node from the old node
    newMat = copyMat(oldNode.matrix)
    newMat[oldEmptyTile[0]][oldEmptyTile[1]], newMat[newEmptyTile[0]][newEmptyTile[1]] = newMat[newEmptyTile[0]][newEmptyTile[1]], newMat[oldEmptyTile[0]][oldEmptyTile[1]]
    newFi = oldNode.fi + 1
    newCi = calcCi(newFi, newMat)
    newNode = Node(oldNode, newMat, newEmptyTile, noNode, newCi, newFi, movement)
    return newNode

def checkIndex(emptyTile):
    return (emptyTile[0] >= 0 and emptyTile[0] < 4 and emptyTile[1] >= 0 and emptyTile[1] < 4)

def checkKurang(mat):
    # check value of Sigma Kurang(i) + X which determines
    # if the puzzle is solvable or not
    tableKurang = []
    totalKurang = 0
    for i in range(4):
        for j in range(4):
            # check for one tile
            kurang = 0
            if mat[i][j] != -1:
                for k in range(j+1, 4):
                    if (mat[i][k] < mat[i][j] and mat[i][k] != -1):
                        kurang += 1
                for k in range(i+1, 4):
                    for l in range(4):
                        if (mat[k][l] < mat[i][j] and mat[k][l] != -1):
                            kurang += 1
                tableKurang.append([mat[i][j], kurang])
            else:
                for k in range(j+1, 4):
                    if (mat[i][k] < 16):
                        kurang += 1
                for k in range(i+1, 4):
                    for l in range(4):
                        if (mat[k][l] < 16):
                            kurang += 1
                tableKurang.append([16, kurang])
                # + X if in index selected, otherwise don't add 1
                if ((i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0)):
                    totalKurang += 1
            totalKurang += kurang
    
    if (totalKurang % 2 == 0):
        return True, tableKurang, totalKurang
    else:
        return False, tableKurang, totalKurang

def nPuzzleSolver(tempMat, tempEmptyTilePos):
    start = time.time()
    # Check if the puzzle is solvable or not
    isSolvable, tableKurang, totalKurang = checkKurang(tempMat)
    tableKurang = sorted(tableKurang, key=lambda x: x[0])

    if (isSolvable):
        ctr_node = 1
        # Create Root Node
        rootNode = Node(None, tempMat, tempEmptyTilePos, ctr_node, calcCi(0, tempMat), 0, None)

        # Create Priority Queue
        pq = PriorityQueue()
        pq.push((rootNode.ci, rootNode))

        # List of additions to directions empty tile movement: up right down left
        add_row = [-1, 0, 1, 0]
        add_col = [0, 1, 0, -1]

        # Tree making & Solution searching
        while (not(pq.isEmpty())):
            # Pop the node with the lowest cost
            ci, currentNode = pq.pop()
            
            # Check if the node is the goal node
            if (isGoal(currentNode.matrix)):
                # Found the Solution
                end = time.time()
                print()
                print("Initial configuration:")
                printMatrix(tempMat)
                print()
                print("Value of each element's Kurang(i):")
                printTableKurang(tableKurang)
                print()
                print("Sigma Kurang(i) from 1 to 16 + X = " + str(totalKurang))
                print()
                print("Steps : [ ", end="")
                printPath(currentNode)
                print(" ]")
                print()
                print("Execution time: " + str(end-start))
                print()
                print("Number of generated nodes: " + str(ctr_node))
                break
            else:
                for i in range(4):
                    if ((currentNode.movement == None) or (currentNode.movement == 0 and i != 2) or (currentNode.movement == 2 and i != 0) 
	                    or (currentNode.movement == 1 and i != 3) or (currentNode.movement == 3 and i != 1)):
                        tempEmptyTilePos = (currentNode.emptyTilePos[0] + add_row[i], currentNode.emptyTilePos[1] + add_col[i])

                        if(checkIndex(tempEmptyTilePos)):
                            # Create Node
                            ctr_node += 1
                            childNode = deriveNode(currentNode, currentNode.emptyTilePos, tempEmptyTilePos, ctr_node, i)

                            pq.push((childNode.ci, childNode))
    else:
        print("The puzzle is not solvable")
        print("Value of each element's Kurang(i):")
        printTableKurang(tableKurang)
        print("Sigma Kurang(i) from 1 to 16 + X = " + str(totalKurang))

# MAIN PROGRAMME

# Variables Used
cntLine = 0
tempMat = [[0]*4]*4
tempEmptyTilePos = (0, 0)
not_found = True

# Ask for input data choice
choice = int(input("1. Input from randomizer\n2. Input from file\n"))

if (choice == 1):
    randomData = random.sample(range(16), 16)
    for i in range(4):
        for j in range(4):
            if (randomData[i*4+j] == 0):
                randomData[i*4+j] = -1
                tempEmptyTilePos = (i, j)
            tempMat[i][j] = randomData[i*4+j]
else:
    # Ask for file name input (including extension)
    fileName = input("Enter file name: ")

    # Read from File and Store to Matrix
    file = open(fileName, "r")
    lines = file.readlines()
    
    for line in lines:
        # remove newline
        line = line.rstrip()
        # split to list of integers
        tempMat[cntLine] = [int(x) for x in line.split()]
        if (not_found):
            for i in range(len(tempMat[cntLine])):
                if (tempMat[cntLine][i] == -1):
                    not_found = False
                    tempEmptyTilePos = (cntLine, i)
        cntLine += 1

nPuzzleSolver(tempMat, tempEmptyTilePos)