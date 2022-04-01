class Node:
    def __init__(self, parentNode, matrix, emptyTilePos, noNode, ci, fi):
        # parent node
        self.parentNode = parentNode
        # matrix of the puzzle
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         self.matrix[i][j] = matrix[i][j]
        self.matrix = matrix
        # tuple containing empty tile position in matrix
        self.emptyTilePos = emptyTilePos
        # node number
        self.noNode = noNode
        # cost of the node
        self.ci = ci
        # depth of the node from the root node
        self.fi = fi
        # movement made to this node from this node's parent
        # self.movement = movement
    
    def __lt__(self, next):
        return self.ci < next.ci