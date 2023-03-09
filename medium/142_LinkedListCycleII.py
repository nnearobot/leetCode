# 142. Linked List Cycle II
# Medium
# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        addressMap = set()
        node = head
        while node is not None:
            if node in addressMap:
                return node
            addressMap.add(node)
            node = node.next

        return None