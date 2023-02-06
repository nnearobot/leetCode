# 876. Middle of the Linked List
# Easy
# https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nextHead = head
        nodeCount = 1
        while nextHead.next != None:
            nodeCount += 1
            nextHead = nextHead.next

        count = 0
        nodeCount = nodeCount // 2
        print(nodeCount)
        nextHead = head
        while count < nodeCount:
            nextHead = nextHead.next
            count += 1

        return nextHead

