# 958. Check Completeness of a Binary Tree
# medium
# https://leetcode.com/problems/check-completeness-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [(root, 0, 0)]
        curLvl = count = 0
        prevNum = -1
        while len(q) > 0:
            node, lvl, num = q.pop(0)
            if lvl == curLvl:
                count += 1
                if num != prevNum + 1:
                    return False
            else:
                if count != math.pow(2, curLvl):
                    return False
                if num != 0:
                    return False
                curLvl += 1
                count = 1

            prevNum = num         
            if node.left:
                q.append((node.left, curLvl + 1, num * 2))
            if node.right:
                q.append((node.right, curLvl + 1, num * 2 + 1))

        return True