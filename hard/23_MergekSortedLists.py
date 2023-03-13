# 23. Merge k Sorted Lists
# Hard
# https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        for l in lists:
            if l:
                q.append(l)
        if len(q) == 0:
            return None

        while len(q) > 1:
            node1 = q.pop(0)
            node2 = q.pop(0)
            res = node = ListNode()
            while node1 or node2:
                node.next = ListNode()
                if node2 and (not node1 or node2.val < node1.val):
                    node.next.val = node2.val
                    node2 = node2.next
                else:
                    node.next.val = node1.val
                    node1 = node1.next
                node = node.next
            q.append(res.next)
        
        return q.pop(0)
