# 530. Minimum Absolute Difference in BST
# Easy
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        q = []
        q.append(root)
        nodeSet = set()

        while len(q) > 0:
            node = q.pop(0)
            nodeSet.add(node.val)
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)
        
        res = 100001
        nodeSet = sorted(nodeSet)
        for i, num in enumerate(nodeSet):
            if i == 0:
                continue
            diff = abs(num - nodeSet[i - 1])
            res = min(res, diff)

        return res
