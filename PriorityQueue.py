from heapq import heappop, heappush

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, key):
        heappush(self.heap, key)
    
    def pop(self):
        return heappop(self.heap)
    
    def isEmpty(self):
        return (not(self.heap))

    def length(self):
        return len(self.heap)