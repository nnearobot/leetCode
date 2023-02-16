# 104. Maximum Depth of Binary Tree
# Easy
# https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        q = []
        q.append([root, 1])
        res = 1
        while len(q) > 0:
            nodePair = q.pop(0)
            node = nodePair[0]
            level = nodePair[1]
            res = max(res, level)
            if node.left != None:
                q.append([node.left, level + 1])
            if node.right != None:
                q.append([node.right, level + 1])
        
        return res