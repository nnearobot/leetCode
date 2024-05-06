# 2487. Remove Nodes From Linked List
# medium
# https://leetcode.com/problems/remove-nodes-from-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        right_node = self.removeNodes(head.next)
        if right_node.val <= head.val:
            head.next = right_node
            return head
        return right_node
