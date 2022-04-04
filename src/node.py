# Node to store the puzzle state at a time
class node:
    def __init__(self, parent, matrix, emptyTile, noNode, movement, level, cost):
        # Parent Node
        self.parent = parent
        # Puzzle state in matrix
        self.matrix = matrix
        # Tuple (row, column) of the empty tile's location
        self.emptyTile = emptyTile
        # Number of node
        self.noNode = noNode
        # Movement that generates this node from the parent
        self.movement = movement
        # Level of the node
        self.fi = level
        # Cost
        self.ci = cost
    
    def __lt__(self, other):
        # Comparation done by cost
        return self.ci < other.ci