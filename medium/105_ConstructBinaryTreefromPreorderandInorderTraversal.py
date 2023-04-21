# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def getTree(current_inorder: List[int]) -> Optional[TreeNode]:
            nonlocal preorder_index
            if (preorder_index >= len(preorder)):
                return None

            node = TreeNode()
            node.val = preorder[preorder_index]
            head_index = current_inorder.index(node.val)
            list_left = current_inorder[0:head_index]
            list_right = current_inorder[head_index + 1:]
            if len(list_left) > 0:
                preorder_index += 1
                node.left = getTree(list_left)
            if len(list_right) > 0:
                preorder_index += 1
                node.right = getTree(list_right)
            return node

        preorder_index = 0
        return getTree(inorder)
