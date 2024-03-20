# 1669. Merge In Between Linked Lists
# medium
# https://leetcode.com/problems/merge-in-between-linked-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node_res = list1
        node = node_res
        node_next = node_res.next
        counter = 0
        while counter < b:
            if counter == a - 1:
                node.next = list2
                node_last = node.next
                while node_last.next:
                    node_last = node_last.next
            
            node = node_next
            node_next = node_next.next
            counter += 1

        node_last.next = node_next

        return node_res