# 1026. Maximum Difference Between Node and Ancestor
# medium
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        q = []
        q.append((root, root.val, root.val)) # cur_val, min_val, max_val
        max_diff = 0
        while len(q) > 0:
            data = q.pop()
            for node in [data[0].left, data[0].right]:
                if node:
                    min_val = min(node.val, data[1])
                    max_val = max(node.val, data[2])
                    max_diff = max(max_diff, max_val - min_val)
                    q.append((node, min_val, max_val))
        return max_diff