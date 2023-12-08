# 606. Construct String from Binary Tree
# easy
# https://leetcode.com/problems/construct-string-from-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = str(root.val)

        if root.left == None and root.right == None:
            return res

        res += '(' + self.tree2str(root.left) + ')' if root.left != None else '()'
        res += '(' + self.tree2str(root.right) + ')' if root.right != None else ''

        return res
