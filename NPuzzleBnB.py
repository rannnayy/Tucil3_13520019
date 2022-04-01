from numpy import dtype
from PriorityQueue import PriorityQueue
from Node import Node
import time
import heapq as hq

goal_path = []

def printPath(node):
    # print the path from the root node to the goal node
    if (node.parentNode != None):
        printPath(node.parentNode)
    goal_path.append(node.noNode)
    print(node.noNode)
    print(node.matrix)
    print("\n")

def isGoal(matrix):
    # check if the puzzle is solved
    for i in range(4):
        for j in range(4):
            if (i != 3 and j != 3):
                if (matrix[i][j] != (i * 4 + j + 1)):
                    return False
            else:
                if (matrix[i][j] != -1):
                    return False
    return True

def calcGi(matrix):
    # calculate misplaced tiles
    ctr = 1
    misplaced = 0
    #ans = [[1,2,3,4], [5,6,7,8], [10,11,12,13], [14,15,16,-1]]
    for i in range(4):
        for j in range(4):
            if (i != 3 and j != 3):
                if (matrix[i][j] != ctr):
                    misplaced += 1
            else:
                if (matrix[i][j] != 0):
                    misplaced += 1
            ctr += 1
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

# MAIN PROGRAMME

# Ask for file name input (including extension)
fileName = input("Enter file name: ")

# Read from File and Store to Matrix
file = open(fileName, "r")
lines = file.readlines()
cntLine = 0
tempMat = [[0]*4]*4
tempEmptyTilePos = [0, 0]
not_found = True
for line in lines:
    # remove newline
    line = line.rstrip()
    # split to list of integers
    # tempMat[cntLine] = list(map(int, line.split()))
    tempMat[cntLine] = [int(x) for x in line.split()]
    print(tempMat[cntLine])
    if (not_found):
        for i in range(4):
            if (tempMat[cntLine][i] == -1):
                not_found = False
                tempEmptyTilePos = [cntLine, i]
    cntLine += 1

print("Initial configuration:")
for i in range(4):
    for j in range(4):
        print(tempMat[i][j], end=" ")
    print()

start = time.time()
# Check if the puzzle is solvable or not
isSolvable, tableKurang, totalKurang = checkKurang(tempMat)
# tableKurangSorted = hq.heapify(tableKurang)
print(totalKurang)
print(isSolvable)
print("Value of each element's Kurang(i):")
print(tableKurang)

if (isSolvable):
    ctr_node = 1
    # Create Root Node
    rootNode = Node(None, tempMat, tempEmptyTilePos, ctr_node, calcCi(0, tempMat), 0, None)
    print(tempEmptyTilePos)
    print()
    print(rootNode.noNode)
    for a in range (4):
        for b in range(4):
            print(rootNode.matrix[a][b], end=" ")
        print()
    print()

    # Create Priority Queue
    pq = PriorityQueue()
    pq.push(rootNode)

    # List of additions to directions empty tile movement: up right down left
    add_row = [-1, 0, 1, 0]
    add_col = [0, 1, 0, -1]

    counter = 0
    # Tree making & Solution searching
    while (not(pq.isEmpty()) and counter < 10):
        # print("flag 1")
        # Pop the node with the lowest cost
        currentNode = pq.pop()
        print(pq.length())
            
        print()
        if (currentNode.parentNode != None):
            print(currentNode.parentNode.noNode)
        print(currentNode.noNode)
        for a in range (4):
            for b in range(4):
                print(currentNode.matrix[a][b], end=" ")
            print()
        print()
        
        # print("flag 2")
        # Check if the node is the goal node
        if (isGoal(currentNode.matrix)):
            # print("flag 3")
            # Found the Solution
            end = time.time()
            print("Value of each element's Kurang(i):")
            print(tableKurang)
            print("Sigma Kurang from 1 to 16 + X: " + str(totalKurang))
            printPath(currentNode)
            print("Execution time: " + str(end-start))
            print("Number of generated nodes: " + str(ctr_node))
            break
        else:
            # print("flag 4")
            # create child nodes in 4 directions
            # up right down left
            # 0  1     2    3
            # illegal moves
            # 0 -> 2
            # 2 -> 0
            # 1 -> 3
            # 3 -> 1
            # invalid movement if currentNode.movement 
            for i in range(4):
                if ((currentNode.movement == 0 and i != 2) or (currentNode.movement == 2 and i != 0) 
                    or (currentNode.movement == 1 and i != 3) or (currentNode.movement == 3 and i != 1)):
                    # print("flag 5" + str(i))
                    tempEmptyTilePos = [currentNode.emptyTilePos[0] + add_row[i], currentNode.emptyTilePos[1] + add_col[i]]
                    print(currentNode.emptyTilePos)
                    print(tempEmptyTilePos)

                    if(checkIndex(tempEmptyTilePos)):
                        # print("flag 6" + str(i))
                        tempMat = copyMat(currentNode.matrix)
                        tempMat[currentNode.emptyTilePos[0]][currentNode.emptyTilePos[1]] = currentNode.matrix[tempEmptyTilePos[0]][tempEmptyTilePos[1]]
                        tempMat[tempEmptyTilePos[0]][tempEmptyTilePos[1]] = -1

                        # Create Node
                        ctr_node += 1
                        childNode = Node(currentNode, tempMat, tempEmptyTilePos, ctr_node, calcCi(currentNode.fi + 1, tempMat), currentNode.fi + 1, i)
                        print(pq.length())
                        print()
                        print(childNode.parentNode.noNode)
                        print(childNode.noNode)
                        for a in range (4):
                            for b in range(4):
                                print(childNode.matrix[a][b], end=" ")
                            print()
                        print()

                        pq.push(childNode)
                else:
                    print("Same movement as before")
                    # print("flag 5" + str(i))
                    tempEmptyTilePos = [currentNode.emptyTilePos[0] + add_row[i], currentNode.emptyTilePos[1] + add_col[i]]
                    print(currentNode.emptyTilePos)
                    print(tempEmptyTilePos)

                    if(checkIndex(tempEmptyTilePos)):
                        # print("flag 6" + str(i))
                        tempMat = copyMat(currentNode.matrix)
                        tempMat[currentNode.emptyTilePos[0]][currentNode.emptyTilePos[1]] = currentNode.matrix[tempEmptyTilePos[0]][tempEmptyTilePos[1]]
                        tempMat[tempEmptyTilePos[0]][tempEmptyTilePos[1]] = -1

                        # Create Node
                        ctr_node += 1
                        childNode = Node(currentNode, tempMat, tempEmptyTilePos, ctr_node, calcCi(currentNode.fi + 1, tempMat), currentNode.fi + 1, i)
                        print()
                        print(childNode.parentNode.noNode)
                        print(childNode.noNode)
                        for a in range (4):
                            for b in range(4):
                                print(childNode.matrix[a][b], end=" ")
                            print()
                        print()

                        # pq.push(childNode)
        counter += 1
else:
    print("The puzzle is not solvable")
    print("Value of each element's Kurang(i):")
    print(tableKurang)
    print("Sigma Kurang from 1 to 16 + X: " + str(totalKurang))