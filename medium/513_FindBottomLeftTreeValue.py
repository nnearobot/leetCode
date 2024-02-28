# 513. Find Bottom Left Tree Value
# medium
# https://leetcode.com/problems/find-bottom-left-tree-value/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        level = -1
        val = root.val
        q = collections.deque()
        q.append((root, 0)) # node, level
        while len(q) > 0:
            (node, lvl) = q.popleft()
            if lvl > level:
                val = node.val
                level = lvl
            if node.left:
                q.append((node.left, lvl + 1))
            if node.right:
                q.append((node.right, lvl + 1))
        return val
