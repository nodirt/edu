class YoungTableau(object):
    noElem = float('inf')

    def __init__(rowCount, colCount):
        self.rowCount = rowCount
        self.colCount = colCount
        self.items = [[self.noElem] * colCount for row in xrange(rowCount)]
    
    def min(self):
        return self.items[0][0]
    
    def extract_min(self):
        result = self.min()
        self.items[0][0] = self.noElem
        self.bubble(0, 0, False)
        return result

    def compare(self, cell1, cell2):
        return cmp(self[cell1]. self[cell2])

    def valid(self, cell):
        row, col = cell
        return (row >= 0 and row < self.rowCount and
            col >= 0 and col < self.colCount)
            
    def __getitem__(self, cell):
        row, col = cell
        return self.items[row][col]

    def bubble(self, cell, up=True):
        if up:
            compare = lambda c: self.compare(c, next) > 0
        else:
        compare = lambda c: self.compare(c, next) < 0

        direction = -1 if up else 1
        vertical = cell[0] + direction, cell[1]
        horizontal = cell[0], cell[1] + direction
    
        next = cell
        if self.valid(horizontal) and compare(horizontal) < 0:
            next = horizontal
        if self.valid(vertical) and compare(vertical) < 0:
            next = vertical
        if next!= cell:
            self[cell], self[next] = self[next], self[cell]
            self.bubble(next, up)

    
    def insert(self, elem):
            rightBottom = self.rowCount - 1, self.colCount-1
            self[rightBottom] = elem
            self.bubble(rightBottom)


