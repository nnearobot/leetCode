"""
116. Populating Next Right Pointers in Each Node
Medium
https://leetcode.com/problems/populating-next-right-pointers-in-each-node



# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None

        q = []
        q.append([root, 0])
        prevLvl = -1
        tmpNode = None
        while len(q) > 0:
            nodePair = q.pop(0)
            node = nodePair[0]
            lvl = nodePair[1]
            if lvl != prevLvl:
                prevLvl = lvl
                node.next = None
            else:
                node.next = tmpNode

            tmpNode = node
            if node.right:
                q.append([node.right, lvl + 1])
            if node.left:
                q.append([node.left, lvl + 1])
        
        return root