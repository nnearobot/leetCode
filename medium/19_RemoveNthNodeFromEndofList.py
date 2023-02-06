"""
19. Remove Nth Node From End of List
Medium
https://leetcode.com/problems/remove-nth-node-from-end-of-list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nextHead = head
        nodeCount = 1
        while nextHead.next != None:
            nodeCount += 1
            nextHead = nextHead.next

        if (nodeCount == n) :
            return head.next

        count = 0
        nodeCount = nodeCount - n - 1
        nextHead = head
        while count < nodeCount:
            nextHead = nextHead.next
            count += 1
        nextHead.next = nextHead.next.next

        return head
