# 543. Diameter of Binary Tree
# easy
# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def calculateLongestPathWithNode(node: Optional[TreeNode]):
            nonlocal longest_path

            if not node:
                return 0

            left = 1 + calculateLongestPathWithNode(node.left) if node.left else 0
            right = 1 + calculateLongestPathWithNode(node.right) if node.right else 0
            longest_path = max(longest_path, left + right)

            return max(left, right)

        longest_path = 0
        calculateLongestPathWithNode(root)
        return longest_path
