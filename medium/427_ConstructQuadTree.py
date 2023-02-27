"""
427. Construct Quad Tree
Medium
https://leetcode.com/problems/construct-quad-tree

"""

'''
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
'''

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def getQuad(rowStart, rowEnd, colStart, colEnd) -> 'Node':
            if rowStart == rowEnd and colStart == colEnd:
                return Node(grid[rowStart][colStart], True, None, None, None, None)
            
            rowMiddleStart = (rowEnd - rowStart) // 2 + rowStart
            rowMiddleEnd = rowMiddleStart + 1
            colMiddleStart = (colEnd - colStart) // 2 + colStart
            colMiddleEnd = colMiddleStart + 1

            tL = getQuad(rowStart, rowMiddleStart, colStart, colMiddleStart)
            tR = getQuad(rowStart, rowMiddleStart, colMiddleEnd, colEnd)
            bL = getQuad(rowMiddleEnd, rowEnd, colStart, colMiddleStart)
            bR = getQuad(rowMiddleEnd, rowEnd, colMiddleEnd, colEnd)

            if tL.val == tR.val == bR.val == bL.val and tL.isLeaf and tR.isLeaf and bL.isLeaf and bR.isLeaf:
                return Node(tL.val, True, None, None, None, None)
            
            return Node(1, False, tL, tR, bL, bR)
        
        n = len(grid) - 1
        return getQuad(0, n, 0, n)
