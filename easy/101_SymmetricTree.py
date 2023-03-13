# 101. Symmetric Tree
# Easy
# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = []
        q.append([root.left, 1])
        q.append([root.right, 1])
        lvl = 1
        vals = []
        while len(q) > 0:
            nodePair = q.pop(0)
            node = nodePair[0]
            curLvl = nodePair[1]
            if curLvl != lvl:
                n = len(vals)
                for i in range(n // 2):
                    if vals[i] != vals[n - i - 1]:
                        return False
                vals = []
                lvl += 1
            vals.append(node.val if node != None else 1000)
            if node != None:
                q.append([node.left, curLvl + 1])
                q.append([node.right, curLvl + 1])

        return True
