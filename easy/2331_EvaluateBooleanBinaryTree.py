# 2331. Evaluate Boolean Binary Tree
# easy
# https://leetcode.com/problems/evaluate-boolean-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return root.val == 1

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        return left or right if root.val == 2 else left and right