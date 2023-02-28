"""
652. Find Duplicate Subtrees
Medium
https://leetcode.com/problems/find-duplicate-subtrees
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        treeMap = {}
        def checkTree(root) -> str:
            if root == None:
                return '/null'
            struct = str(root.val)
            struct += '/' + checkTree(root.left)
            struct += '/' + checkTree(root.right)
            if struct not in treeMap:
                treeMap[struct] = 0
            elif treeMap[struct] == 1:
                res.append(root)
            treeMap[struct] += 1
            return struct
        
        checkTree(root)
        
        return res