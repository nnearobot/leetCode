# 129. Sum Root to Leaf Numbers
# Medium
# https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def getPath(node, arr):
            nonlocal res
            if node.left == None and node.right == None:
                num = node.val
                p = 10
                for i in range(len(arr) - 1, -1, -1):
                    num += arr[i] * p
                    p *= 10
                res += num
                return
            arr.append(node.val)
            if node.left != None:
                getPath(node.left, arr)
            if node.right != None:
                getPath(node.right, arr)
            arr.pop()
        
        getPath(root, [])
        return res