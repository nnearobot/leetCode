# 103. Binary Tree Zigzag Level Order Traversal
# Medium
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q = []
        q.append([root, 0])
        res = []
        while len(q) > 0:
            nodePair = q.pop(0)
            node, lvl = nodePair[0], nodePair[1]
            if lvl >= len(res):
                res.append([])
            if lvl % 2 == 1:
                res[lvl].insert(0, node.val)
            else:
                res[lvl].append(node.val)
            
            if node.left != None:
                q.append([node.left, lvl + 1])
            if node.right != None:
                q.append([node.right, lvl + 1])

        return res