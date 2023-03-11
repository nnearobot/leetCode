# 109. Convert Sorted List to Binary Search Tree
# Medium
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head == None:
            return None
        
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next

        def createNode(s, e) -> TreeNode:
            m = s + math.ceil((e - s) / 2)
            node = TreeNode(arr[m])
            if s == e:
                return node

            node.left = createNode(s, m - 1)
            if m < e:
                node.right = createNode(m + 1, e)
            return node
        
        return createNode(0, len(arr) - 1)