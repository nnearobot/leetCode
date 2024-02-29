# 1609. Even Odd Tree
# medium
# https://leetcode.com/problems/even-odd-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        prev_level = -1
        val = root.val
        q = collections.deque()
        q.append((root, 0)) # node, level
        while len(q) > 0:
            (node, lvl) = q.popleft()
            if lvl % 2:
                if node.val % 2:
                    return False
                if node.val >= val and lvl == prev_level:
                    return False
            else:
                if node.val % 2 == 0:
                    return False
                if node.val <= val and lvl == prev_level:
                    return False

            if lvl > prev_level:
                prev_level = lvl
            val = node.val
                
            if node.left:
                q.append((node.left, lvl + 1))
            if node.right:
                q.append((node.right, lvl + 1))
        
        return True
